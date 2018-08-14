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

gA = s2data.get_dict_gA()
gB = s2data.get_dict_gB()

################################################################
print("[#] Analyzing gA Data:")

gA_statistics = {
    "outCitations": []
}
 
for paper in tqdm(gA.values()):
    # citation count
    outcites = len(paper["outCitations"])
    gA_statistics["outCitations"].append(outcites)

################################################################
print("[#] Analyzing gA Data:")

gB_statistics = {
    "inCitations": [],
    "years": []
}

for paper in tqdm(gB.values()):
    # citation count
    incites = len(paper["inCitations"])
    gB_statistics["inCitations"].append(incites)
    # years
    if "year" in paper: gB_statistics["years"].append(paper["year"])

################################################################
print("[#] Writing Results:")

# gA : outCitations
fig, ax = plt.subplots(tight_layout=True)
data = np.array(gA_statistics["outCitations"])
data = data / data.max() # normalize
ax.hist(data , bins=n_bins)
# TODO
# ax.vlines(x, ymin, ymax, colors='k', linestyles='solid', label='', *, data=None, **kwargs)
# x : scalar or 1D array_like
# x-indexes where to plot the lines.
# ymin, ymax : scalar or 1D array_like
# Respective beginning and end of each line. If scalars are provided, all lines will have same length.
# colors : array_like of colors, optional, default: 'k'
# linestyles : ['solid' | 'dashed' | 'dashdot' | 'dotted'], optional
# label : string, optional, default: ''

plt.show()
quit()

# gB : inCitations
fig, ax = plt.subplots(tight_layout=True)
data = np.array(gB_statistics["inCitations"])
data = data / data.max() # normalize

# gB : year
fig, ax = plt.subplots(tight_layout=True)
data = np.array(gB_statistics["year"])
data = data / data.max() # normalize
