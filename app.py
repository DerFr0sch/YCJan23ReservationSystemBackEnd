from flask import Flask
from flask_cors import CORS, cross_origin
import getKamerinfo


app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getKamerinfo/<zoekterm>")
def showKamerinfo(zoekterm):
    return getKamerinfo.getKamerinfo(zoekterm)