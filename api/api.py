import os
import flask
import base64
import time
import json

from werkzeug.datastructures import FileStorage

from flask_thumbnails import Thumbnail
from flask import Flask, flash, request, redirect, render_template, url_for, jsonify
from werkzeug.utils import secure_filename

import filteringManager
import folderManager
import dataIndexer

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = b'seksiseks'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi'}
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 4
homeDir="C:\\inetpub\\wwwroot\\Unsecure\\TESTAPI\\"

@app.route('/test', methods=['GET','POST'])
def test():
    return "a"
@app.route('/upload/', methods=['GET','POST'])
def uploadPage():
    if request.method == 'POST':
        ##if(True):
        ##    return "0"
        tags = request.form.get('tags')
        tags = str(tags).split(' ')
        f = request.files['image']
        ## fire wla
    ##    return (str(f) + " " + str(f.read()))
    ##    return "1"
        ## stupid bonk*
        dataIndexer.updateIntellisense(tags)
        tags.insert(0, '')
        
        newFileName = str(base64.b64encode((str(time.time())+f.filename+str(time.time())).encode('ascii'))[-16:])[1:99]
        newFileName = newFileName[1:len(newFileName)-1]
        newFileExtension = f.filename.split('.')[-1:len(f.filename.split('.'))][0]
        jsonFile = open(folderManager.emptyFolder()+newFileName+ ".txt", 'w')
        
        jsonFile.write(str(tags))
        ##-DĞZENLEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
        ##+tabi lordum :3
        jsonFile.write("\n"+newFileExtension)
        jsonFile.close()
        ##-burada dosyanın json kısmının da göndermeyi ayarla lütfen :(( .save yemedi :SSS
        ##+önemli değil aşkısı <3
        f.save(folderManager.emptyFolder()+newFileName+ "." + newFileExtension)

        returnText = "<style>body{font-size:1.45em}</style><b style='font-size:1.35em;'>"+f.filename+"</b> is uploaded to server's local filesystem as ``<b style='font-size:1.25em;'>"+newFileName+"."+newFileExtension+"</b>``<br><br><div style='height:1px;padding:0px;margin:5px;font-size:1.20em'>With the tags under;</div>"
        for i in range(len(tags)):
            returnText += "<p style='padding:0px;margin:2px;height:30px;margin-left:18px;font-size:1.25em'><b style='font-size:2.2em'>.&nbsp;</b> "+tags[i]+"<br>"
        return returnText
    page = open(homeDir+"sites\\upload.html",'r')
    return page.read()

@app.route('/filter/', methods=['GET','POST'])
def filterPage():
    page = open(homeDir+"sites\\filter.html",'r')
    if request.method == 'POST':
        contentFilter = flask.request.values.get('tags').split(' ')
        content,listedTags = filteringManager.showFiltered(contentFilter)
        
        contentReturnText = "<img src='"
        tagsReturnText = ""
        counter=0
        for i in content:
            
            if (counter%2!=0):
                if (i == 'mp4' or i == 'mov' or i == 'avi'):
                    contentReturnText = contentReturnText[:-10]
                    contentReturnText += "<video controls src='http://127.0.0.1:80\\Unsecure\\TESTAPI\\data\\"+(fileName+str(i)).split('data\\')[1]+"'></video><img src='"
                else:
                    contentReturnText += "http://127.0.0.1:80\\Unsecure\\TESTAPI\\data\\"+(fileName+str(i)).split('data\\')[1]+"'><img src='"
            else:
                fileName = str(i)[:-3]
            counter+=1
        for j in listedTags:
            if(j=="''"):
                tagsReturnText += "- all<br>"
            else:
                tagsReturnText += "- "+j[1:-1]+"<br>"
                finalTag = j
            
        
        if (finalTag == "'Not us but chickens...'"):
            returnPage = str(page.read()).split('<ContentBreaker>')
            returnPage = returnPage[0]+returnPage[1]
            returnPage = returnPage.split('<TaglistBreaker>')
            returnPage = returnPage[0]+tagsReturnText+returnPage[1]
            returnPage = returnPage.split('<ChickenBreaker>')
            returnPage = returnPage[0]+"<image class='dancinChicken' src='http://127.0.0.1:80\\Unsecure\\TESTAPI\\pub\\chicken.gif'>"+returnPage[1]
        
        else:
            returnPage = str(page.read()).split('<ContentBreaker>')
            returnPage = returnPage[0]+contentReturnText+returnPage[1]
            returnPage = returnPage.split('<TaglistBreaker>')
            returnPage = returnPage[0]+tagsReturnText+returnPage[1]
            returnPage = returnPage.split('<ChickenBreaker>')
            returnPage = returnPage[0]+returnPage[1]

        return returnPage
        ##return str(flask.request.values.get('tags'))
    return page.read()

@app.route('/', methods=['GET'])
def home():
    page = open(homeDir+"sites\\home.html")
    return page.read()
@app.route('/reload', methods=["GET"])
def reload():
    return str(dataIndexer.createIntellisense())+"<script>setTimeout(function(){window.location.href = 'http://127.0.0.1:5000/'},1000)</script>"
app.run()

