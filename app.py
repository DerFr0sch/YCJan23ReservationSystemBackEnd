from flask import Flask, request
from flask_cors import CORS, cross_origin
import getKamerinfo
import sendKamerinfo
import dbreserveerkamer
import dbfetchkamer
import dbboekkamer
import sendGastgegevens
import getgeboekteKamerinfo
import felix

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getKamerinfo/<zoekterm>")
def showKamerinfo(zoekterm):
    return getKamerinfo.getKamerinfo(zoekterm)

@app.route("/getgeboekteKamerinfo/<zoekterm>")
def showgeboekteKamerinfo(zoekterm):
    return getgeboekteKamerinfo.getgeboekteKamerinfo(zoekterm)

@app.route("/sendKamerinfo")
def storeKamerinfo():
    type = str(request.args.get('ftype'))
    prijs = str(request.args.get('fprijs'))
    beschrijving = str(request.args.get('fbeschrijving'))
    foto = str(request.args.get('ffoto'))
    nummer = str(request.args.get('fnummer'))
    return sendKamerinfo.sendKamerinfob(type,prijs,beschrijving,foto,nummer)

@app.route("/dbreserveerkamer/<kamerid>")
def reserveerKamer(kamerid):
    return dbreserveerkamer.sendKamerreservering(kamerid)

@app.route("/dbfetchkamer/<kamerid>")
def fetchKamer(kamerid):
    return dbfetchkamer.getSpecifickamer(kamerid)

@app.route("/sendGastgegevens")
def storeGastgegevens():
    voornaam = str(request.args.get('kvoornaam'))
    achternaam = str(request.args.get('kachternaam'))
    voorvoegsel = str(request.args.get('kvoorvoegsel'))
    postcode = str(request.args.get('kpcode'))
    adres = str(request.args.get('kadres'))
    land = str(request.args.get('kland'))
    tel = str(request.args.get('ktel'))
    email = str(request.args.get('kemail'))
    betaalmethode = str(request.args.get('kbetaalmethode'))
    boekKamer()
    return sendGastgegevens.sendGastgegevensdb(voornaam, achternaam, voorvoegsel, postcode, adres, land, tel, email, betaalmethode)
    
def boekKamer():
    kamerid = str(request.args.get('kamerid'))
    totprijs = str(request.args.get('totaleprijs'))
    boeking_begin = str(request.args.get('kbegindat'))
    boeking_eind = str(request.args.get('keinddat'))
    betaalmet = str(request.args.get('kbetaalmethode'))
    return dbboekkamer.sendKamerboeking(kamerid, totprijs, boeking_begin, boeking_eind, betaalmet)

@app.route("/testfelix")
def testfelix():
    return felix.testfelixinfile(12, 1200, 11112023, 11112023, "ideal")