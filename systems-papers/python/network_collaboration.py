"""

Creates a network of author collaboration.

- Nodes are identified by the respective author's names.
- Edges are identified by the key of the paper that it represents collaboration on, with an 
  integer suffix to distinguish the many edges resulting from one paper collaboration. For 
  example, a paper with three authors results in three edges, since each author collaborated 
  with each other author once.

"""

# utilities
import os
import utils.shared_utils as utils
import utils.combinatorics as combos
from tqdm import tqdm

# modules
from gexf.gexf import GEXF
import utils.data as u_data
import authors.authors_stats as a_stats

# graph init
graph = GEXF("network_collaboration")
graph.setAttribute("graph", "defaultedgetype", "undirected")

hindecies = a_stats.getAllAuthorHIndeces()

# iterate through papers
conf_filenames = u_data.getConferenceFilenames()
features = a_stats.getAllAuthorFeatures()
for conf_filename in conf_filenames:
    data = u_data.getPapers(conf_filename)
    papers = data['papers']
    for paper in papers:
        paper_key    = paper['key'] # String
        author_names = [ a_stats.getAuthorUName(a,features) for a in paper['authors']] # [String]
        uid_suffix   = 0 # unique integer suffix to distinguish edges created by this paper
        for (a1,a2) in combos.pairs_unordered(author_names):
            if a1 > a2: a1, a2 = a2, a1 # put in alphabetical order
            # attributes
            a1_attrs, a2_attrs = {}, {}
            if a1 in hindecies: a1_attrs["hindex"] = hindecies[a1]
            if a2 in hindecies: a2_attrs["hindex"] = hindecies[a2]
            # add to graph
            graph.addNode(a1)
            graph.addNode(a2)
            graph.addEdge(paper_key+"_"+str(uid_suffix), a1, a2, 1)
            uid_suffix += 1

# graph.write("/Users/Henry/Documents/Drive/SystemsAnalysis/systems-papers/gexf/")