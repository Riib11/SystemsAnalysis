import xml.etree.ElementTree as ET
import os
import papers.paper_data as paper_data
import utils.xml as xml

total_citations_count = 0

papers_filenames = paper_data.getPaperFilenames_XML()
print("len(papers) =",papers_filenames)

for fn in papers_filenames:
    root = xml.parseXML(fn)
    try:
        reflist = xml.getDescendantByTagPath(root, ["back","ref-list"])
        total_citations_count += len(reflist)
    except:
        pass

print("total citations count:", total_citations_count)