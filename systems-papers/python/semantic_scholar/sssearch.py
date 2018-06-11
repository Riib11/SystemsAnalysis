import utils.shared_utils as utils
import papers.paper_features as p_features
import os
import json
from tqdm import tqdm


def load_json_file(fn, force=True):
    try:
        with open(fn, mode="r", encoding='utf-8') as f:
            return json.load(f)
    except OSError:
        print("Couldn't read file ", fn);
        if force:
            raise
        else:
            return {}

# def createSSDatabase(dirname):
#     filenames = os.listdir(dirname)


def safeDictCheck(d,k,target):
    if not k in d: return False
    value = d[k]
    return value == target

# src: https://stackoverflow.com/questions/2460177/edit-distance-in-python
def editdist(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

class SSSearch:

    def __init__(self, dirname, threshold):
        self.dirname = dirname
        self.threshold = threshold
        self.entries = []

    def loadfile(self, filename):
        file = open(self.dirname + filename, "r+", encoding="utf-8")
        self.entries = json.load(file)
        file.close()

    def query(self,authors,title,year):
        filenames = os.listdir(self.dirname)
        possibles = [] # entry objects
        distances = [] # total distance score for each object
        for filename in filenames:
            if not filename.endswith(".json"): continue
            self.loadfile(filename)
            for entry in tqdm(self.entries):
                # year (have to get this right)
                if True: # safeDictCheck(entry,"year",year):
                    dist = (
                        # title
                        editdist(entry["title"],title) +
                        # authors
                        min([ editdist(auth1["name"],a2)
                            for auth1 in entry["authors"]
                            for a2 in authors ]))
                    # threhold
                    if dist <= self.threshold:
                        possibles.append(entry)
                        distances.append(dist)

        # get min
        i_min = 0
        dist_min = self.threshold
        for i in range(len(distances)):
            d = distances[i]
            if d < dist_min:
                dist_min = d
                i_min = i
        print(len(possibles))
        return possibles[i_min], dist_min