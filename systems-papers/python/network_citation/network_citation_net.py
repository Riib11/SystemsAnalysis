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
from utils.strings import clean
from tqdm import tqdm

# modules
from gexf.gexf import GEXF
from net.net import NET
import utils.data as u_data
import papers.paper_features as p_features

def generate():
    
    # graph init
    graph = NET("network_citation_net")

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
            title = clean(paper["title"])
            # make node for paper
            graph.addNode(title, {
                "conference" : conf_name,
                "title"      : title,
                "key"        : key
            })
            # make citation edges
            e_id = key
            uid_suffix = 0
            for t in p_features.getCitationsTitles(key):
                t = clean(t)
                graph.addNode(t)
                graph.addEdge(e_id+str(uid_suffix), title, t, 1)
                uid_suffix += 1


    print("------------------------------------------------")
    print("[%] Writing file:")
    graph.write("/Users/Henry/Documents/Drive/SystemsAnalysis/systems-papers/net/")
