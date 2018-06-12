import utils.shared_utils as utils
import semantic_scholar.sssearch as sssearch

semantic_scholar_dir = "/data/sda/semanticscholar/"
# semantic_scholar_dir = "/Users/Henry/Documents/Drive/SystemsAnalysis/systems-papers/semantic-scholar/"

s3 = sssearch.SSSearch(
    semantic_scholar_dir,
    {
        "year"   : 1,
        "title"  : 50,
        "author" : 50,
    },
    True
)

result, dist = s3.query(
    ["Svilen Kanev", "Sam Xi", "Gu-Yeon Wei", "David Brooks"],
    "Mallacc: Accelerating Memory Allocation",
    "2017"
)

print(dist,":",result["title"])

# utils.save_json_file(
#     "/Users/Henry/Downloads/result.json",
#     result)