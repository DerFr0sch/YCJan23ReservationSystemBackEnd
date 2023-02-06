import mysql.connector

url = 'http://localhost:5000/sendKamerinfo/'
myobj = ('kamer type', 'kamer prijs')


def sendKamerinfob(type,prijs,beschrijving,foto,nummer):
    con = mysql.connector.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()

    # type = abc
    # prijs = 25
    # beschrijving = "mooie kamertje"
    # foto = "hotel.jpg"
    # nummer = 455
    sql = "INSERT INTO hotelkamer (kamertype, prijs, beschrijving, kamerfoto, kamernummer) VALUES (%s, %s, %s, %s, %s)"
    val = (type, prijs, beschrijving, foto, nummer)
    mycursor.execute(sql, val)
    #print(val,flush=True)
    con.commit()
    print(mycursor.rowcount, "kamer toegevoegd")
    return "opgeslagen"

#sendKamerinfo("test1")
