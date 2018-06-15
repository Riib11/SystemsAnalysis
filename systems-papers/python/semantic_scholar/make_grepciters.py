import semantic_scholar.s2data as s2data
import utils.data as u_data
from tqdm import tqdm
import math

fn_grepciters = u_data.systems_papers_directory+"script/grepciters.sh"

# script
grepciters = open(fn_grepciters,"w+")

# loop through titles of papers
cfns = [ fn for fn in u_data.getConferenceFilenames() ]
last_i = len(cfns)-1

# start index
i = 43


cfns = cfns[i:] # already did the first 43

per_part = 8                        # processer per partition
parts = math.ceil(len(cfns)/parts)  # number of partitions
part_i = 0                          # index of partition
part_j = 0                          # index within partition


for cfn in tqdm(cfns):
    
    cname = cfn.replace(".json","")
    data = u_data.getPapers(cfn)
    papers = data["papers"]

    cmd = ''

    if part_i == 0:
        cmd += '\n\nnohup echo "starting section ' + str(part_j) + '"'
        cmd += ' & grep -h'
    else:
        cmd += ' & grep -h'

    for p in papers:
        title = p["title"].replace('"','\\"')
        cmd += ' -e "' + title + '"'

    cmd += ' ' + u_data.semantic_scholar_dir + 's2-corpus-*.json'
    cmd += ' > ' + s2data.makeCitersCnfFn(i)

    # write cmd
    grepciters.write(cmd)

    # increment
    i      += 1
    part_i += 1
    if part_i == per_part:
        part_i = 0
        part_j += 1

grepciters.write(
    '\n\necho "[Done] Don\'t forget to concat the output and format it and everything!"')

grepciters.close()
