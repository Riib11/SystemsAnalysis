import semantic_scholar.s2data as s2data
import utils.shared_utils as utils
import utils.data as u_data
import math
from tqdm import tqdm

fn_grepciteds = u_data.systems_papers_directory+"script/grepciteds.sh"
grepciteds = open(fn_grepciteds,"w+")

# list of cited ids
citedslist = s2data.getCitedsList()

# organize into grep-sections
per_grep = 100
greps_n = math.ceil(len(citedslist)/per_grep)
greps = []
i = 0
for cited_id in tqdm(citedslist):
    if i == 0: greps.append([])
    greps[-1].append(cited_id)
    i += 1
    if i == per_grep: i = 0

# organize into parallel parts
per_part = 8
parts_n = math.ceil(greps_n/per_part)
part_i = 0 # index of partition
part_j = 0 # index within partition

for grep in tqdm(greps):

    cmd = ''

    if part_i == 0:
        cmd += '\n\nnohup echo "starting setion ' + str(part_j) + '"'
        cmd += ' & grep -h'
    else:
        cmd += ' & grep -h'

    for cited_id in grep:
        cmd += " -e '\"id\": \"" + cited_id + "\"'"

    cmd += ' ' + u_data.semantic_scholar_dir + 's2-corpus-*.json'
    cmd += ' > ' + s2data.makeCitedsSecFn(i)

    grepciteds.write(cmd)

    # increment
    i      += 1
    part_i += 1
    if part_i == per_part:
        part_i = 0
        part_j += 1