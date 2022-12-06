from flask import Flask
import requests
import json
import re

#This is just a set of test end points so I can validate things look good and that the install looks correct.

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/testWiki")
def extractFromURL():
    x = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Yoshua_Bengio&rvlimit=1&formatversion=2&format=json&rvprop=content")
    result = str(x.status_code)
    return x.json()



#Extract all the content
@app.route("/testExtract")
def extractKeyInfo():
    x = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Yoshua_Bengio&rvlimit=1&formatversion=2&format=json&rvprop=content")
    jsonExtract = x.json()

    content = jsonExtract['query']['pages'][0]['revisions'][0]['content']

    return content



#Navigate to the area of the content
@app.route("/testShortDesc")
def extractShortDescription():
    x = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Yoshua_Bengio&rvlimit=1&formatversion=2&format=json&rvprop=content")
    
    #Grab the json
    jsonExtract = x.json()

    #grab the content from the page id
    content = jsonExtract['query']['pages'][0]['revisions'][0]['content']

    #grab the location of the short description
    finalString = content[content.find("{{Short description|")+len('{{Short description|'):content.rfind("}}")]

    print ("String found "+ finalString)
    return finalString



#Navigate to the area of the content
@app.route("/testGetTitle")
def extractTitle():
    x = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Yoshua_Bengio&rvlimit=1&formatversion=2&format=json&rvprop=content")
    
    #Grab the json
    jsonExtract = x.json()

    #grab the title of the page (which also turns out to be the name of the person)
    content = jsonExtract['query']['pages'][0]['title']

    print (content)
    return content



#Extract the short description
@app.route("/testCombineResults")
def getShortDesc():

    #Get the data from the endpoint
    x = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Yoshua_Bengio&rvlimit=1&formatversion=2&format=json&rvprop=content")
    result = str(x.status_code)
    
    #Grab the json
    jsonExtract = x.json()

    #grab the content from the page id
    pageTitle = jsonExtract['query']['pages'][0]['title']

    content = jsonExtract['query']['pages'][0]['revisions'][0]['content']
    findFirstOccurance = content.find("}}")

    print (findFirstOccurance)
    #grab the location of the short description
    finalString = content[content.find("{{Short description|")+len('{{Short description|'):findFirstOccurance]
    shortDesc = finalString.replace('|','')
    print (finalString)

    #It turns out some of the time the | will still come into the results; I just shortcut this by getting rid of this in the final results.
    return (pageTitle + " "+ shortDesc)




