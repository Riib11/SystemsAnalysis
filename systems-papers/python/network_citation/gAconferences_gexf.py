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
    graph = GEXF("citations_gAconferences")
    # parameters
    graph.setParameter("graph", "defaultedgetype", "directed")
    # attributes
    graph.addAttribute( "node" , "outCitations"  , "float"  , "0.0" )
    graph.addAttribute( "node" , "selfCitations" , "float"  , "0.0" )
    graph.addAttribute( "node" , "color"         , "string" , "0000FF" )


    # TODO: color attribute for each paper
    # TODO: print statisics:

    ################################################################
    print("[#] Loading Data:")
    
    gA = s2data.get_dict_gA()
    gB = s2data.get_dict_gB()

    ################################################################
    print("[#] Analyzing Data:")

    # { conference : [selfCitation, outCitations] }
    conferences = {}

    def safeindex(d,k):
        if not k in d: d[k] = [0,0]
        return d[k]

    for id, paper in gA.items():
        conf = conf_utils.normalize_conference(
            paper["venue"])
        if len(conf) == 0: continue
        for target_id in paper["outCitations"]:
            try:
                target_paper = gB[target_id]
                target_conf = conf_utils.normalize_conference(
                    target_paper["venue"])
                if len(target_conf) == 0: continue
                if conf == target_conf:
                    safeindex(conferences,conf)[0] += 1
                else:
                    safeindex(conferences,conf)[1] += 1
            except: pass

    ################################################################
    print("[#] Writing file:")

    selfCitations_list = [ conferences[k][0] for k in conferences.keys() ]
    color_attribute_min = min(selfCitations_list)
    color_attribute_max = max(selfCitations_list)

    def colorAttributeToColor(val):
        norm = (val - color_attribute_min) / color_attribute_max
        return u_colors.RGBToHexColor(norm, 0.0, 1-norm)

    # nodes
    for conf, citations in conferences.items():
        graph.addNode(conf, {
            "selfCitations" : str(citations[0]),
            "outCitations"  : str(citations[1]),
            "color"         : colorAttributeToColor(citations[0])
        })

    # edges (only between members of gA)
    for id, paper in gA.items():
        conf = conf_utils.normalize_conference(
            paper["venue"])
        if len(conf) == 0: continue
        for target_id in paper["outCitations"]:
            try:
                target_paper = gB[target_id]
                target_conf = conf_utils.normalize_conference(
                    target_paper["venue"])
                if len(target_conf) == 0: continue
                # paper in gA
                if target_conf in conferences and conf != target_conf:
                    graph.addEdge(id, conf, target_conf)
            except: pass


    graph.write("../gexf/")

generate()
