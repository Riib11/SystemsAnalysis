"""

Read in authors' data

nodes: authors
edges: collaboration of the connected authors on a paper

"""

import json

data_directory    = "/Users/Henry/Documents/Drive/SystemsAnalysis/systems-papers/authors/data/"
authors_directory = data_directory + "authors/"
conf_directory    = data_directory + "conf/"

def fileToString(path):
    try:
        with open(path, 'r') as file:
            s = ""
            for line in file: s += line
            return s
    except:
        print("[!] Problem reading file at: " + path)

def getData(path):
    data_raw = fileToString(path)
    return json.loads(data_raw)

# example:
if 0:
    data = getData(conf_directory+"ASPLOS.json")
    print(data['key'])