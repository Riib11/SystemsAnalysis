import semantic_scholar.s2data as s2data
import utils.shared_utils as utils

citersdict = {}

s2data.getCiters()
quit()
for c in s2data.getCiters():
    citersdict[ c["id"] ] = c

utils.save_json_file( s2data.citersdict_fn, citersdict )
