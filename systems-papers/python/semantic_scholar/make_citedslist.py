import semantic_scholar.s2data as s2data
import utils.shared_utils as utils
from itertools import chain
from tqdm import tqdm

# set of ids
cited_ids = set({})
for c in tqdm(s2data.getCiters()):
    # get the id's of the citeds
    cited_ids = set(chain(c["outCitations"],cited_ids))

# convert back to list
cited_ids = list(cited_ids)

# save
utils.save_json_file( s2data.citedslist_fn , cited_ids )