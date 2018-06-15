import semantic_scholar.s2data as s2data
import utils.shared_utils as utils
from tqdm import tqdm

citersdict = {}

for c in tqdm(s2data.getCiters()):
    citersdict[ c["id"] ] = c

utils.save_json_file( s2data.citersdict_fn, citersdict )
