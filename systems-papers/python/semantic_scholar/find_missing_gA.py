import semantic_scholar.s2data as s2data
import utils.data as u_data
from tqdm import tqdm
import re
import math
import json

#
# Goal:
#   find the citers that weren't grepped into `citersdict`
#

# DEPRECATED
# compile all of the s2 corpus files
# together into one big megafile, so its
# faster to grep it for titles
#

citersdict = s2data.getCitersDict()
citers_string = str(citers)

#
# search for all the papers
#

missing = {}

# loop through titles of papers
cfns = [ fn for fn in u_data.getConferenceFilenames() ]
last_i = len(cfns) - 1

# start index
i = 0

cfns = cfns[i:] # already did the first 43

for cfn in tqdm(cfns):
    
    cname = cfn.replace(".json","")
    data = u_data.getPapers(cfn)
    papers = data["papers"]

    for p in papers:
        title = p["title"].replace('"','\\"')
        find = re.search(title, citers_string)
        if find==None: missing[p["title"]] = p

json.dump(missing, open(u_data.semantic_scholar_proccessed_dir+"missing_gA.json","w+"))