import utils.data as data

def getBibtex(paper_id):
    with open(data.papers_directory + paper_id + ".bibtex", 'r') as file:
        lines = []
        start = True
        for line in file:
            line = line.strip()
            if start:
                if line.startswith("@article"):
                    start = False
                else:
                    lines.append(line)
            else:
                if line.startswith("}"):
                    start = True
        return lines


def getBibtexValue(line):
    i = line.index("{")
    line = line[i+1:]
    i = line.index("}")
    line = line[:i]
    return line

def getCitationsTitles(paper_id):
    bibtex = getBibtex(paper_id)
    titles = []
    
    inside = False
    for line in bibtex:
        if not inside:
            if line.startswith("@proceedings"):
                inside = True
        else:
            if line.startswith("title"):
                titles.append(getBibtexValue(line))
            elif line.startswith("}"):
                inside = False
    
    return titles

def getCitationsData(paper_id):
    bibtex = getBibtex(paper_id)
    data = {"author":[],"journal":[],"title":[],"year":[]}
    keys = data.keys()
    inside = False
    for line in bibtex:
        if not inside:
            inside = line.startswith("@proceedings")
        else:
            if line.startswith("}"): inside = False
            else:
                value = getBibtexValue(line)
                for key in keys:
                    if line.startswith(key):
                        data[key].append(value)
    return data