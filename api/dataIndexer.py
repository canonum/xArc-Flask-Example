import pathlib
import flask
from flask import jsonify
import json

homeDir="C:\\inetpub\\wwwroot\\Unsecure\\TESTAPI\\api\\"
homePath = pathlib.Path(homeDir+"..\\data")
metaDataFormat = "txt"

def createIntellisense():
    data={}
    for j in homePath.iterdir():
        if(j.is_dir()):
            for k in pathlib.Path(j).iterdir():
                if(str(k)[-3:] == metaDataFormat):
                    file = open(k,'r')
                    tags = str(file.readline())[1:-2].split(', ')
                    ##extension = str(file.readline())
                    for i in tags:
                        if i[1:-1] not in data:
                            
                            data.update({str(i)[1:-1]:1})
                        else:
                            data.update({str(i)[1:-1]:data.get(i[1:-1])+1})
    print(data)
    file = open(homeDir+"..\\data.json","w")
    file.write(json.dumps(data))
    file.close()
    return(data) 

def updateIntellisense(tags):
    return True
    file = open(homeDir+"..\\data.json","r")
    data = file.read()
    file.close()
    data = json.loads(data)
    file = open(homeDir+"..\\data.json","w")
    for i in tags:
        print(i)
        print(data.get(i))
        data.update({i[:data.get(i)]+1})
    file.write(json.dumps(data))
    return(data)
    file.close()
