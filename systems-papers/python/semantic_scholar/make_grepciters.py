import semantic_scholar.s2data as s2data
import utils.data as u_data
from tqdm import tqdm
import math

fn_grepciters = u_data.systems_papers_directory+"script/grepciters.sh"

# script
grepciters = open(fn_grepciters,"w+")

# loop through titles of papers
cfns = [ fn for fn in u_data.getConferenceFilenames() ]
last_j = 0 # len(cfns)-1

# start index
i = 0


cfns = cfns[i:] # already did the first 43

per_part = 8                            # processer per partition
parts = math.ceil(len(cfns)/per_part)   # number of partitions
part_i = 0                              # index within partition
part_j = 0                              # index of partition


for cfn in tqdm(cfns):
    
    cname = cfn.replace(".json","")
    data = u_data.getPapers(cfn)
    papers = data["papers"]

    cmd = '#!/bin/bash' + '\n'

    if part_i == 0:
        cmd += 'echo "starting section ' + str(part_j) + '"'
        cmd += ' & grep -i -h'
    else:
        cmd += ' & grep -i -h'

    for p in papers:
        title = p["title"].replace('"','\\"')
        cmd += " -e '\"id\":\"" + title + "\"'"

    cmd += ' ' + u_data.semantic_scholar_dir + 's2-corpus-*.json'

    datafile_fn = s2data.makeCitersCnfFn(i)

    # write finds to file
    cmd += ' > ' + datafile_fn

    # log the files that have problems
    cmd += '\n'
    cmd += "count=$(wc -l " + datafile_fn + " )"
    cmd += "target='" + str(len(papers)) + "'"
    cmd += "if [ $count != $target ]; then "
    cmd += "echo " + datafile_fn + " has an incorrect number of results > " + datafile_fn+"_errors " + "\nfi\n"

    # write cmd
    grepciters.write(cmd)

    # increment
    i      += 1
    part_i += 1
    if part_j == last_j: break
    if part_i == per_part:
        part_i = 0
        part_j += 1

grepciters.close()
