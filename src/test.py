from flask import Flask
import requests
import json

#This is just a set of test end points so I can validate things look good and that the install looks correct.

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/testWiki")
def extractFromURL():
    x = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Yoshua_Bengio&rvlimit=1&formatver sion=2&format=json&rvprop=content")
    result = str(x.status_code)
    return x.json()

@app.route("/testExtract")
def extractKeyInfo():
    x = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Yoshua_Bengio&rvlimit=1&formatver sion=2&format=json&rvprop=content")
    result = str(x.status_code)
    jsonExtract = x.json()
    #print (jsonExtract['query']['pages']['47749536'])


    #first element in the embedded message from Wikipedia -- We need to know the page id to get to the entry point of the rest of the data
    firstElem = list(jsonExtract['query']['pages'].keys())[0]

    titleName = jsonExtract['query']['pages'][firstElem]['title']

    content = jsonExtract['query']['pages'][firstElem]['revisions'][0]['*']


    
    print(firstElem)
    print(titleName)
    print(content)
    return jsonExtract

