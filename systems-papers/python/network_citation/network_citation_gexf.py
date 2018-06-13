"""

Creates a network of paper citations.

- Info:

    - Nodes represent an individual paper, which may or may not be in the data set.

    - Edges are directed and represent the source paper's citation of the target paper.

"""

# utilities
import sys
import os
import numpy as np
import utils.shared_utils as utils
import utils.colors as u_colors
import utils.combinatorics as u_combos
from tqdm import tqdm

# modules
from gexf.gexf import GEXF
import utils.data as u_data
import papers.paper_features as p_features

def generate():
    
    # graph init
    graph = GEXF("network_citation")
    # parameters
    graph.setParameter("graph", "defaultedgetype", "directed")
    # attributes
    graph.addAttribute( "node", "conference" , "string", "" )
    graph.addAttribute( "node", "title"      , "string", "" )

    # TODO: color attribute for each paper
    # TODO: print statisics:

    # iterate through papers
    conf_filenames = [ fn for fn in u_data.getConferenceFilenames() ]
    conf_filenames = conf_filenames[:10]

    print("------------------------------------------------")
    print("[#] Analyzing Data:")
    for conf_filename in tqdm(conf_filenames):
        conf_name = conf_filename.replace(".json","")
        data = u_data.getPapers(conf_filename)
        papers = data['papers']
        for paper in papers:
            key = paper["key"]
            title = paper["title"]
            graph.addNode(key, {
                "conference" : conf_name,
                "title"      : title
            })
            e_id = key
            uid_suffix = 0
            for title in p_features.getCitationsTitles(key):
                graph.addNode(title, { "title":title })
                graph.addEdge(e_id+str(uid_suffix), key, title, 1)
                uid_suffix += 1


    print("------------------------------------------------")
    print("[%] Writing file:")
    graph.write(u_data.systems_papers_directory + "gexf/")
