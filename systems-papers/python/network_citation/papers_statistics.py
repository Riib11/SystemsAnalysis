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


################################################################
print("[#] Loading Data:")

gA = s2data.get_dict_gA()
gB = s2data.get_dict_gB()

################################################################
print("[#] Analyzing gA Data:")

statistics = {}

def increment_entry(d, k):
    k = k.lower()
    if not k in d: d[k] = 0
    d[k] += 1


statistics["gA"] = {
    "outCitations": [],
    "titlewords": {}
}
gA_statistics = statistics["gA"]
 
for paper in tqdm(gA.values()):
    # citation count
    outcitationcount = len(paper["outCitations"])
    gA_statistics["outCitations"].append(outcitationcount)
    # title words
    titlewords = paper["title"].split()
    for word in titlewords:
        increment_entry(gA_statistics["titlewords"],word)

################################################################
print("[#] Analyzing gA Data:")

statistics["gB"] = {
    "inCitations": [],
    "inCitationsRate": [],
    "titlewords": {},
    "years": []
}
gB_statistics = statistics["gB"]

for paper in tqdm(gB.values()):
    if not "year" in paper: continue
    # citation count
    incitationcount = len(paper["inCitations"])
    gB_statistics["inCitations"].append(incitationcount)
    gB_statistics["inCitationsRate"].append(
        incitationcount/(1 + 2018 - paper["year"]))
    # title words
    titlewords = paper["title"].split()
    for word in titlewords:
       increment_entry(gB_statistics["titlewords"],word)
    # years
    gB_statistics["years"].append(paper["year"])

################################################################
print("[#] Writing Results:")

with open("../statistics/papers_statistics.txt","w+") as file:
    #
    #
    file.write("################################\n")
    file.write("gA statistics:\n")
    #
    file.write("  + outCitation counts:\n")
    file.write("  |     mean : "+str(
        np.mean(gA_statistics["outCitations"]))+"\n")
    file.write("  |   median : "+str(
        np.median(gA_statistics["outCitations"]))+"\n")
    file.write("  |      std : "+str(
        np.std(gA_statistics["outCitations"]))+"\n")
    #
    file.write("  + top couple title words:\n")
    def get(i): return i[1]
    titlewords = sorted(list(gA_statistics["titlewords"].items()), key=get)
    titlewords_len = len(titlewords)
    for i in range(1,100+1): file.write("  |   "+str(i)+". ["+str(np.round(titlewords[-i][1]/titlewords_len, 3))+"] "+titlewords[-i][0]+"\n")

    #
    #
    file.write("################################\n")
    file.write("gB statistics:\n")
    #        
    file.write("  + inCitation/year counts:\n")
    file.write("  |     mean : "+str(
        np.mean(gB_statistics["inCitations"]))+"\n")
    file.write("  |   median : "+str(
        np.median(gB_statistics["inCitations"]))+"\n")
    file.write("  |      std : "+str(
        np.std(gB_statistics["inCitations"]))+"\n")
    
    file.write("  + publish years:\n")
    file.write("  |     mean : "+str(
        np.mean(gB_statistics["years"]))+"\n")
    file.write("  |   median : "+str(
        np.median(gB_statistics["years"]))+"\n")
    file.write("  |      std : "+str(
        np.std(gB_statistics["years"]))+"\n")

    file.write("  + top couple title words:\n")
    titlewords = sorted(list(gB_statistics["titlewords"].items()), key=get)
    titlewords_len = len(titlewords)
    for i in range(1,100+1): file.write("  |   "+str(i)+". ["+str(np.round(titlewords[-i][1]/titlewords_len, 3))+"] "+titlewords[-i][0]+"\n")

    # dump to json
    json.dump(statistics,
        open("../statistics/papers_statistics.json", "w+"))