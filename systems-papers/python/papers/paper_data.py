import utils.data as data

def getPaperFilenames_XML():
    return [ data.paperdata_directory+fn
             for fn in os.listdir(data.paperdata_directory)
             if fn.endswith(".cermxml") ]

