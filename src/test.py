from flask import Flask
import requests
import jsonify

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