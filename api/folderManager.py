import pathlib

homeDir="C:\\inetpub\\wwwroot\\Unsecure\\TESTAPI\\api\\"
homePath = pathlib.Path(homeDir+"..\\data")
folderMaxItemCount =16






def emptyFolder():
    lastFolderNumber = 0
    currentFolder = 0
    isPathList = []
    safePath = ""
    for i in homePath.iterdir():
        if (i.is_dir()):
            lastFolderNumber+=1
            currentFolder = 0
            for path in pathlib.Path(i).iterdir():
                safePath = path
                currentFolder+=1
                if currentFolder>=folderMaxItemCount*2:
                    break
            if currentFolder!=folderMaxItemCount*2:
                return str(i) +"\\"
    returnPath = pathlib.Path(homeDir+"..\\data\\"+str(lastFolderNumber))
    returnPath.mkdir(parents=True, exist_ok=True)
    return str(returnPath) +"\\"

def indexFolderMetadata():
    return True
