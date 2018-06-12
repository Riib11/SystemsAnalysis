import os
import multiprocessing as mp
from tqdm import tqdm

semantic_scholar_dir = "/data/sda/semanticscholar/"

def formatRecord(fn):
    if not fn.startswith("s2-corpus"): return
    if fn.endswith(".json"): return
    lines = None
    with open(semantic_scholar_dir + fn, "r+") as file:
        lines = [ l for l in file ]
    with open(semantic_scholar_dir + fn + ".json", "w+") as file:
        file.write("[\n")
        for i in range(len(lines)):
            l = lines[i]
            if l.endswith("}\n") and i < len(lines)-1:
                l = l[:-1]
                file.write(l+",\n")
            else:
                file.write(l)
        file.write("\n]\n")

filenames = os.listdir(semantic_scholar_dir)

for fn in tqdm(filenames):
    formatRecord(fn)

# processes = [mp.Process(target=formatRecord, args=(fn,)) for fn in filenames]

# for p in processes: p.start()
# for p in processes: p.join()

print("Done!")