from gexf import GEXF

g = GEXF("codetest")
g.setAttribute("graph", "defaultedgetype", "undirected")

size  = 10
nodes = [ str(x) for x in range(size) ]
for i in range(size):
    g.addNode(nodes[i])
    g.addEdge(str(i), nodes[i], nodes[(i+1)%size])

g.write("/Users/Henry/Documents/Drive/SystemsAnalysis/systems-papers/gexf")