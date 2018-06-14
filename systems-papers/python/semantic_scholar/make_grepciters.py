import semantic_scholar.s2data as s2data
import utils.data as u_data
from tqdm import tqdm

fn_grepciters = u_data.systems_papers_directory+"script/grepciters.sh"

# script
grepciters = open(fn_grepciters,"w+")
# remvove old data file
grepciters.write("rm "+s2data.citers_fn+"\n")

# loop through titles of papers
cfns = [ fn for fn in u_data.getConferenceFilenames() ]
i = 0
l = len(cfns)-1
for cfn in tqdm(cfns):
    cname = cfn.replace(".json","")
    data = u_data.getPapers(cfn)
    papers = data["papers"]
    for p in papers:
        title = p["title"].replace('"','\\"')
        grepciters.write('grep -h "' + title + '"' +
            u_data.semantic_scholar_dir + '*.json >>' + # search raw data
            s2data.citers_fn + '\n' # put results into citers.json
        # ../semantic-scholar/*.json >> citers.json\n') # this was old approach

        grepciters.write('echo "['+str(i)+'/'+str(l)+'] '+title+'"\n')
    i += 1

grepciters.write(
    'echo "[!] Don\'t forget to format '+fn_citersjson+
    'with the array brackets and remove ending comma!"')

grepciters.close()
