from flask import Flask
import felix
import vossa
import daan

app = Flask(__name__)

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