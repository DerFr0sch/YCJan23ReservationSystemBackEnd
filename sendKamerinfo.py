import mysql.connector
import mariadb

def sendKamerinfob(abc):
    con = mariadb.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()

    type = abc
    prijs = 25
    beschrijving = "mooie kamertje"
    foto = "hotel.jpg"
    nummer = 455
    sql = "INSERT INTO hotelkamer (kamertype, prijs, beschrijving, kamerfoto, kamernummer) VALUES (%s, %s, %s, %s, %s)"
    val = (type, prijs, beschrijving, foto, nummer)
    mycursor.execute(sql, val)

    con.commit()
    print(mycursor.rowcount, "kamer toegevoegd")
    return "opgeslagen"

#sendKamerinfo("test1")
