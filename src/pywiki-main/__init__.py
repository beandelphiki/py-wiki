from flask import Flask
import os

app = Flask(__name__)

app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 5001)))