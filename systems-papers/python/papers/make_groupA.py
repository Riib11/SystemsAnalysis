import xml.etree.ElementTree as ET
import os
from tqdm import tqdm

import papers.paper_data as paper_data
import utils.data as data
import utils.xml as xml

total_citations_count = 0
total_errors_count = 0

papers_filenames = paper_data.getPaperFilenames_XML()
print("len(papers) =",papers_filenames)

for fn in tqdm(papers_filenames):
    root = xml.parseXML(fn)
    try:
        reflist = xml.getDescendantByTagPath(root, ["back","ref-list"])
        total_citations_count += len(reflist)
    except:
        total_errors_count += 1

print("total citations count:", total_citations_count)
print("total errors count:", total_errors_count)