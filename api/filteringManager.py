import pathlib

homeDir="C:\\inetpub\\wwwroot\\Unsecure\\TESTAPI\\api\\"
homePath = pathlib.Path(homeDir+"..\\data")
metaDataFormat = "txt"

def showFiltered(filters):
    shownContent = []
    listedTags = []
    for i in filters:
        for j in homePath.iterdir():
            if(j.is_dir()):
                for k in pathlib.Path(j).iterdir():
                    if(str(k)[-3:] == metaDataFormat):
                        file = open(k,'r')
                        tags = str(file.readline())[1:-2].split(', ')
                        extension = str(file.readline())
                        tags.append("'"+extension+"'")
                        
                        file.close()
                        for l in tags:
                            if(i == l[1:-1]):
                                listedTags += tags
                                shownContent.append(k)
                                shownContent.append(extension)
                                break


    res = []
    resTag = []
    for j in listedTags:
        if j not in resTag:
            resTag.append(j) 
    for i in range(len(shownContent)):
        if (i*2)+2 > len(shownContent):
            break
        if shownContent[i*2] not in res:
           res.append(shownContent[i*2])
           res.append(shownContent[(i*2)+1])

    if (len(resTag) == 0):
        resTag = ["'Not us but chickens...'"]
    return res,resTag
