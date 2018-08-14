"""

Creates a network of conference citations.

- Info:

    - Nodes represent a conference

    - Edges are directed and one weight point represents one paper in a conference citing another paper in another conference

"""

# utilities
import sys
import os
import numpy as np
import utils.shared_utils as utils
import utils.conf_utils as conf_utils
import utils.colors as u_colors
import utils.combinatorics as u_combos
from tqdm import tqdm

# modules
from gexf.gexf import GEXF
import utils.data as u_data
import semantic_scholar.s2data as s2data

def generate():

    ################################################################
    print("[#] Initializing GEXF")
    
    # graph init
    graph = GEXF("citations_authors")
    # parameters
    graph.setParameter("graph", "defaultedgetype", "directed")
    # attributes
    # graph.addAttribute( "node", "conference" , "string", "" )
    # graph.addAttribute( "node", "title"      , "string", "" )
    # graph.addAttribute( "node", "year"      , "string", "" )


    # TODO: color attribute for each paper
    # TODO: print statisics:

    ################################################################
    print("[#] Loading Data:")
    
    gA = s2data.get_dict_gA()
    gB = s2data.get_dict_gB()

    ################################################################
    print("[#] Analyzing Data:")

    edge_id = 0
    for source_id, source_paper in gA.items():
        source_conf = conf_utils.normalize_conference(
            source_paper["venue"])
        graph.addNode(source_id, {})
        for target_id in source_paper["outCitations"]
            target_conf = normalize_conference(
                gB[target_id]["venue"])
            graph.addNode(target_id, {})
            graph.addEdge(str(edge_id), source_conf, target_conf)
            edge_id += 1

    ################################################################
    print("[#] Writing file:")

    graph.write("/home/blancheh/SystemsAnalysis/systems-papers/gexf/")

generate()
