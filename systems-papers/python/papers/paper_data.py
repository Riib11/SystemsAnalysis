import utils.data as data

def getPaperFilenames_XML():
    return [ fn for fn in os.listdir(data.paperdata_directory) if fn.endswith(".cermxml") ]

