from .xml import XML

class GEXF:

    version = "1.3"

    def __init__(self, name):
        self.name = name
        self.attributes = {
            "gexf"  : {"version":GEXF.version},
            "graph" : {"mode":"static"},
            "nodes" : {},
            "edges" : {}}
        self.nodes = {}
        self.edges = {}

    def setAttribute(self, tag, key, value):
        self.attributes[tag][key] = value

    def addNode(self, id, label=None):
        label = label or id
        self.nodes[id] = {"id": id, "label":label}

    def addEdge(self, id, source, target, weight=1):
        self.edges[id] = {"id": id, "source":source, "target":target, "weight":weight}

    def write(self, directory):
        xml = XML(self.name + ".gexf")
        
        # start gexf
        xml.addHeader("gexf"  , self.attributes["gexf"])
        xml.addHeader("graph" , self.attributes["graph"])

        # nodes
        xml.addHeader("nodes", self.attributes["nodes"])
        for node in self.nodes.values(): xml.addTag("node", node)
        xml.addFooter("nodes")
        # edges
        xml.addHeader("edges", self.attributes["edges"])
        for edge in self.edges.values(): xml.addTag("edge", edge)
        xml.addFooter("edges")
        
        # end gexf
        xml.addFooter("graph")
        xml.addFooter("gexf")

        xml.write(directory)