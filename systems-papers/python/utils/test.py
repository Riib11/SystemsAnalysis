import shared_utils

features = shared_utils.load_csv_file("/Users/Henry/Documents/Drive/SystemsAnalysis/systems-papers/authors/features/authors.csv")

print(shared_utils.author_uname("Vaspol Ruamviboonsuk",features))