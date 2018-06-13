import utils.data as u_data
from tqdm import tqdm

fn_grepciters = u_data.systems_papers_directory+"script/grepciters.sh"
fn_citersjson = "citers.json"

grepciters = open(fn_grepciters,"w+")
grepciters.write("rm "+fn_citersjson+"\n")

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
        grepciters.write('grep -h "'+title +'" ../semantic-scholar/*.json >> citers.json\n')
        grepciters.write('echo "['+str(i)+'/'+str(l)+'] '+title+'"\n')
    i += 1


grepciters.write(
    'echo "[!] Don\'t forget to format '+fn_citersjson+
    'with the array brackets and remove ending comma!"')

grepciters.close()
