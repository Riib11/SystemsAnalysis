class XML:

    indentation = "    "

    def __init__(self, name):
        self.name = name
        self.content = ""
        self.indent_level = 0

    def indent(self):
        self.content += self.indent_level * XML.indentation

    def indentIn(self):
        self.indent()
        self.indent_level += 1

    def indentOut(self):
        self.indent_level -= 1
        self.indent()

    def addHeader(self, tag, attributes):
        self.indentIn()
        header = "<"+tag
        for k,v in attributes.items():
            header += " "+k+"=\""+str(v)+"\""
        header += ">"
        self.content += header + "\n"

    def addFooter(self, tag):
        self.indentOut()
        self.content += "</"+tag+">" + "\n"

    def addTag(self, tag, attributes):
        self.indent()
        tag = "<" + tag
        for k,v in attributes.items():
            tag += " "+k+"=\""+str(v)+"\""
        tag += "/>"
        self.content += tag + "\n"

    def write(self, directory):
        with open(directory + self.name, 'w+') as file:
            file.write(self.content)