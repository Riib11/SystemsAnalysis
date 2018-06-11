import utils.shared_utils as utils
import semantic_scholar.sssearch as sssearch

s3 = sssearch.SSSearch(
    "/Users/Henry/Documents/Drive/SystemsAnalysis/systems-papers/semantic-scholar/",
    {
        "year"   : 1,
        "title"  : 50,
        "author" : 50,
    }
)

result, dist = s3.query(
    ["Kate Jack"],
    "Organizing a search for an academic administrator.",
    "1986"
)

print(dist,":",result["title"])

# utils.save_json_file(
#     "/Users/Henry/Downloads/result.json",
#     result)