from flask import Flask, request
from flask_cors import CORS, cross_origin
import getKamerinfo
import sendKamerinfo
import dbreserveerkamer

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getKamerinfo/<zoekterm>")
def showKamerinfo(zoekterm):
    return getKamerinfo.getKamerinfo(zoekterm)

@app.route("/sendKamerinfo")
def storeKamerinfo():
    type = str(request.args.get('ftype'))
    prijs = str(request.args.get('fprijs'))
    beschrijving = str(request.args.get('fbeschrijving'))
    foto = str(request.args.get('ffoto'))
    nummer = str(request.args.get('fnummer'))
    #return type+prijs+beschrijving+foto+nummer
    return sendKamerinfo.sendKamerinfob(type,prijs,beschrijving,foto,nummer)

@app.route("/dbreserveerkamer/<kamerid>")
def reserveerKamer(kamerid):
    return dbreserveerkamer.sendKamerreservering(kamerid)

