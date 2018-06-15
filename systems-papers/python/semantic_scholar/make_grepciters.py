import semantic_scholar.s2data as s2data
import utils.data as u_data
from tqdm import tqdm

fn_grepciters = u_data.systems_papers_directory+"script/grepciters.sh"

# script
grepciters = open(fn_grepciters,"w+")

# loop through titles of papers
cfns = [ fn for fn in u_data.getConferenceFilenames() ]
i = 43
l = len(cfns)-1

cfns = cfns[i:] # already did the first 43

for cfn in tqdm(cfns):
    cname = cfn.replace(".json","")
    data = u_data.getPapers(cfn)
    papers = data["papers"]

    # grep
    cmd = 'grep -h'
    for p in papers:
        title = p["title"].replace('"','\\"')
        cmd += ' -e "' + title + '"'
    cmd += ' ' + u_data.semantic_scholar_dir + 's2-corpus-*.json'
    cmd += ' > ' + s2data.makeCitersCnfFn(i) + '\n'

    # echo
    cmd += 'echo "['+str(i)+'/'+str(l)+']"\n'

    # write cmd
    grepciters.write(cmd)

    # increment
    i += 1

grepciters.write(
    'echo "[Done] Don\'t forget to concat the output and format it and everything!"')

grepciters.close()
