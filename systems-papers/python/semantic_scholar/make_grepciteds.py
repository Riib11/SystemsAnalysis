import semantic_scholar.s2data as s2data
import utils.shared_utils as utils

# remove old file
grepciteds = open(s2data.citeds_fn,"w+")
grepciteds.write("rm "+s2data.citeds_fn+"\n")

# list of cited ids
citedslist = s2data.getCitedsList()
i,l = 0, len(citedslist)
for cited_id in citedslist:
    # looks like: grep -h '"id": "..." path/*.json >> path/citeds.json'
    grepciteds.write(
        "grep -h '\"id\": \"" + cited_id + "\"'" +
        data.semantic_scholar_dir+"*.json >>" +
        s2data.citeds_fn + "\n" )

    grepciteds.write('echo "['+str(i)+'/'+str(l)+'] '+cited_id+'"\n')