from flask import Flask
from wikiRulesUtils.core import wikiRules
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


    #Clean up the Short Description
    DescriptorSanitized = descriptor.replace('_', ' ')
    finalDescriptor = "{{"+ DescriptorSanitized +"|"
    print (DescriptorSanitized)

    #grab the content from the page id
    content = jsonExtract['query']['pages'][0]['revisions'][0]['content']

    #Run our rules
    shortDescriptionCheck = wikiRules.ruleDescriptorSeach(DescriptorSanitized, content)

    #Check to make sure the ShortDescription is there
    if(shortDescriptionCheck == False):
        return 'That descriptor doesn\'t exist with this current combination; Check your Country Code or Article Spelling'

    #grab the location of the short description
    findFirstOccurance = content.find("}}")
    finalString = content[content.find(finalDescriptor)+len(finalDescriptor):findFirstOccurance]
    
    #Sanitize the output just in case a spare | shows up
    shortDescSanitized = finalString.replace('|','')

    return shortDescSanitized 