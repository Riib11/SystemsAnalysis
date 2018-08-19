#######################################
# Variables of interest:
# - gA:
#     - outCitations
# - gB:
#     - inCitations
#     - year

# utilities
import sys
import os
import json
import numpy as np
import utils.shared_utils as utils
import utils.conf_utils as conf_utils
import utils.colors as u_colors
from tqdm import tqdm

# modules
import utils.data as u_data
import semantic_scholar.s2data as s2data

# matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
np.random.seed(19680801)

################################################################
print("[#] Loading Data:")

statistics = json.load(open("../statistics/papers_statistics.json"))
gA_statistics = statistics["gA"]
gB_statistics = statistics["gB"]

################################################################
print("[#] Writing Results:")

if False:
    # gA : outCitations
    fig, ax = plt.subplots(tight_layout=True)
    
    data = np.array(gA_statistics["outCitations"])
    ax.hist(data , bins=120)
    
    plt.title("Distribution of outCitations in Group A")
    plt.xlabel("number of outCitations")
    plt.ylabel("frequency")
    plt.show()
    # TODO
    # ax.vlines(x, ymin, ymax, colors='k', linestyles='solid', label='', *, data=None, **kwargs)
    # x : scalar or 1D array_like
    # x-indexes where to plot the lines.
    # ymin, ymax : scalar or 1D array_like
    # Respective beginning and end of each line. If scalars are provided, all lines will have same length.
    # colors : array_like of colors, optional, default: 'k'
    # linestyles : ['solid' | 'dashed' | 'dashdot' | 'dotted'], optional
    # label : string, optional, default: ''

if False:
    # gB : inCitationsRate
    fig, ax = plt.subplots(tight_layout=True)
    plt.yscale('log', nonposy='clip')
    
    data = np.array(gB_statistics["inCitationsRate"])
    ax.hist(data , bins=100)
    
    plt.title("Distribution of inCitations per Year in Group B")
    plt.xlabel("inCitations per year after 2018")
    plt.ylabel("frequency")
    plt.show()

if False:
    # gB : inCitations
    fig, ax = plt.subplots(tight_layout=True)
    plt.yscale('log', nonposy='clip')

    data = np.array(gB_statistics["inCitations"])
    ax.hist(data , bins=100)

    plt.title("Distribution of inCitations in Group B")
    plt.xlabel("number of inCitations")
    plt.ylabel("frequency")
    plt.show()

if False:
    # gB : year
    # fig, ax = plt.figure(figsize=(6,6)), plt.axes([0,0,1,1])
    fig, ax = plt.subplots(tight_layout=True)
    
    data = np.array(gB_statistics["years"])
    ax.hist(data , bins=( max(data) - min(data) ))
    
    plt.title("Distribution of Publication Years in Group B")
    plt.xlabel("year published")
    plt.ylabel("frequency")
    plt.show()

if True:
    # gA : author_collaborations
    fig, ax = plt.subplots(tight_layout=True)
    plt.yscale('log', nonposy='clip')
    
    data = np.array(list(gA_statistics["author_collaborations"].values()))
    ax.hist(data , bins=( max(data) - min(data) ))
    
    plt.title("Collaboration Counts of Authors in Group A")
    plt.xlabel("number of collaborations")
    plt.ylabel("frequency")
    plt.show()