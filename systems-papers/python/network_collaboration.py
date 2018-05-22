"""

Creates a network of author collaboration.

- Nodes are identified by the respective author's names.
- Edges are identified by the key of the paper that it represents collaboration on, with an integer suffix to distinguish the many edges resulting from one paper collaboration. For example, a paper with three authors results in three edges, since each author collaborated with each other author once.

"""

# utilities
import os
import utils.shared_utils as utils
import utils.combinatorics as combos
from tqdm import tqdm

# modules
from gexf.gexf import GEXF
import network_collaboration.authors as authors

# graph init
graph = GEXF("network_collaboration")
graph.setAttribute("graph", "defaultedgetype", "undirected")

# iterate through conference files (containing papers)
directory = authors.conf_directory
files     = filter(lambda x : x.endswith(".json"), os.listdir(directory))

# for now, just analyzing a subset of the data
files = files[:10]

for filename in files:
    data = authors.getData(directory + filename)
    papers = data['papers']
    for paper in papers:
        paper_key    = paper['key'] # String
        author_names = [ utils.author_name(a)[0] for a in paper['authors']] # [String]
        uid_suffix   = 0 # unique integer suffix to distinguish edges created by this paper
        for (a1,a2) in combos.pairs_unordered(author_names):
            graph.addNode(a1)
            graph.addNode(a2)
            graph.addEdge(paper_key+"_"+str(uid_suffix), a1, a2)
            uid_suffix += 1

graph.write("/Users/Henry/Documents/Drive/SystemsAnalysis/systems-papers/gexf/")