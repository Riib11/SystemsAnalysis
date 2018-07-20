import xml.etree.ElementTree as ET
import os
import papers.paper_data as paper_data
import utils.xml as xml

total_citations_count = 0

for fn in paper_data.getPaperFilenames_XML():
    root = xml.parseXML(fn)
    try:
        reflist = xml.getDescendantByTagPath(root, ["back","ref-list"])
        total_citations_count += len(reflist)
    except:

print("total citations count:", total_citations_count)