from flask import Flask
from flask_cors import CORS, cross_origin
import felix
import vossa
import daan
import michael


app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/felix")
def vanFelix():
    return felix.vanfelix()

@app.route("/vossa")
def vanVossa():
    return vossa.vanvossa()


@app.route("/daan/<kamernummer>")
def vanDaan(kamernummer):
    return daan.vandaan(kamernummer)


@app.route("/michael/<zoekterm>")
def vanMichael(zoekterm):
    return michael.vanmichael(zoekterm)