from flask import Flask
import requests
import json


app = Flask(__name__)



@app.route("/<title>/countryCode/<countryCode>/descriptor/<descriptor>")
def extractDescription( title:str, countryCode:str, descriptor:str ):
    url = "https://"+countryCode+".wikipedia.org/w/api.php"
    params={
        'action':'query',
        'prop':'revisions',
        'titles': title,
        'rvlimit':'1',
        'formatversion':'2',
        'format': 'json',
        'rvprop':'content'
    }

    x = requests.get(url,params)

    jsonExtract = x.json()

    print (type(jsonExtract))
    #Run our rules

    #Check to make sure the ShortDescription is there


    #Check to make sure the Article is there


    #grab the content from the page id
    content = jsonExtract['query']['pages'][0]['revisions'][0]['content']

    #Clean up the Short Description
    DescriptorSanitized = descriptor.replace('_', ' ')
    finalDescriptor = "{{"+ DescriptorSanitized +"|"


    #grab the location of the short description
    findFirstOccurance = content.find("}}")
    finalString = content[content.find(finalDescriptor)+len(finalDescriptor):findFirstOccurance]
    
    #Sanitize the output just in case a spare | shows up
    shortDescSanitized = finalString.replace('|','')

    return shortDescSanitized 





    def ruleArticleIsMissing(inputJsonObj:dict):
        return 0

    def ruleNoShortDescription():
        return 0

    