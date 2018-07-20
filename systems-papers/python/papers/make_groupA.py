import xml.etree.ElementTree as ET
import os
from tqdm import tqdm
import json

import papers.paper_data as paper_data
import utils.data as data
import utils.xml as xml

papers_directory = data.papergroups_directory
papers_filenames = paper_data.getPaperFilenames_XML()

groupA = []

for fn in tqdm(papers_filenames):
    path = papers_directory + fn
    root = xml.parseXML(path)
    j = xml.XML_to_JSON(root)
    groupA.append(j)

json.dump(groupA, open(paper_data.groupA_fn, "w+"))