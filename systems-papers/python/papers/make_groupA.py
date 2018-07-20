import xml.etree.ElementTree as ET
import os
from tqdm import tqdm
import json

import papers.paper_data as paper_data
import utils.data as data
import utils.xml as xml

papers_directory = data.paperdata_directory
papers_filenames = paper_data.getPaperFilenames_XML()

groupA = []

for fn in tqdm(papers_filenames):
    path = papers_directory + fn
    try:
        root = xml.parseXML(path)
        j = xml.XML_to_JSON(root)
        j["error"] = False
        j["fn"] = fn
        groupA.append(j)
    except:
        j = {"error":True , "fn":fn}
        groupA.append(j)

json.dump(groupA, open(paper_data.groupA_fn, "w+"))