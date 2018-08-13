with open("missing_ids_gA.txt", "r+") as ids:
    with open("grep_missing_gA.sh", "w+") as file:
        for id in ids:
            id = id.strip()
            file.write("grep -h \"\\\"id\\\":\\\"" + id + "\\\"\" /data/sys-papers/semsch/*.json >> missing_gA.json\n")