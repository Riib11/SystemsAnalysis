import json
import os

systems_papers_directory = "../../systems-papers/"

data_directory     = systems_papers_directory+"authors/data/"
authors_directory  = data_directory+"authors/"
conf_directory     = data_directory+"conf/"

features_directory = systems_papers_directory+"authors/features/"

papers_directory   = systems_papers_directory + "sys-papers/"

semantic_scholar_dir = "/data/sys-papers/semsch/"

def fileToString(path):
    try:
        with open(path, 'r') as file:
            s = ""
            for line in file: s += line
            return s
    except:
        print("[!] Problem reading file at: " + path)

def getJSONData(path):
    data_raw = fileToString(path)
    return json.loads(data_raw)

def getJSONFilenames(directory):
    return filter(lambda x : x.endswith(".json") and not x.endswith("template.json"), os.listdir(directory))

def getConferenceFilenames():
    return getJSONFilenames(data_directory+"conf/")

# get json file in data/conf
def getPapers(conf_filename):
    return getJSONData(conf_directory+conf_filename)

# get json file in data/authors
def getAuthors(conf_filename):
    return getJSONData(authors_directory+conf_filename)