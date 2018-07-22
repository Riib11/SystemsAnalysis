import utils.shared_utils as utils
from utils.data import semantic_scholar_proccessed_dir, semantic_scholar_tmp_dir

# Divided Raw Data (lists)

makeCitersCnfFn = lambda i: semantic_scholar_tmp_dir + "citers_cnf" + str(i)
makeCitedsSecFn = lambda i: semantic_scholar_tmp_dir + "citeds_sec" + str(i)

makeGrepMissingGroupAFn = lambda i: semantic_scholar_proccessed_dir + "missingGroupA_part" + str(i)

# Raw Data (list)

citers_fn = semantic_scholar_proccessed_dir + "citers.json"
getCiters = lambda: utils.load_json_file(citers_fn)

citeds_fn = semantic_scholar_proccessed_dir + "citeds.json"
getCiteds = lambda: utils.load_json_file(citeds_fn)

# Processed data (dict)

citersdict_fn = semantic_scholar_proccessed_dir + "citersdict.json"
getCitersDict = lambda: utils.load_json_file(citersdict_fn)

citedsdict_fn = semantic_scholar_proccessed_dir + "citedsdict.json"
getCitedsDict = lambda: utils.load_json_file(citedsdict_fn)

# Just Ids (list)

citedslist_fn = semantic_scholar_proccessed_dir + "citedslist.json"
getCitedsList = lambda: utils.load_json_file(citedslist_fn)

# Missing

missing_groupA_fn = semantic_scholar_proccessed_dir + "missing_groupA.json"
getMissingGroupA = lambda: utils.load_json_file(missing_groupA_fn)

# TODO
missing_groupB_fn = semantic_scholar_proccessed_dir + "missing_groupB.json"
getMissingGroupB = lambda: utils.load_json_file(missing_groupB_fn)

# Missed

missed_outcites_fn = semantic_scholar_proccessed_dir + "missed_outcites.json"
getMissedOutcites = lambda: utils.load_json_file(missed_outcites_fn)
