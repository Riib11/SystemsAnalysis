import utils.data as u_data
import utils.shared_utils as utils
import os

def getAllAuthorFeatures():
    return utils.load_csv_file(u_data.features_directory+"authors.csv")

def getAuthorUName(author, features):
    return utils.author_uname(author, features)

# does full pass through data/conf
def getAllAuthorHIndecies():
    conf_filenames = u_data.getConferenceFilenames()
    hindecies = {}
    for conf_filename in conf_filenames:
        authors = u_data.getAuthors(conf_filename)
        for a_name, a_data in authors.items():
            if isinstance(a_data, str) or not "hindex" in a_data: continue
            h_ind = a_data["hindex"]
            print(h_ind)
            # update existing entry
            if a_name in hindecies:
                prev = hindecies[a_name]
                hindecies[a_name] = max(prev,h_ind)
            # add entry
            else:
                hindecies[a_name] = h_ind
    return hindecies