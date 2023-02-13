import mysql.connector
import json

def testfelixinfile(kamerid, totprijs, boeking_begin, boeking_eind, betaalmet):
    con = mysql.connector.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()
    sql = "INSERT INTO member (voornaam, achternaam, voorvoegsel, adres_straatnaam_huisnummer, adres_postcode, adres_land, telefoonnummer, emailadress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = ("fred", "fred", "van", "straatf", "postcodef", "nederladn", "0612345678", "dig@dag.nl")
    print(val)
    mycursor.execute(sql, val)


    con.commit()
    sql = "SELECT * FROM member ORDER BY member_id DESC"
    
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    print(myresult[0][0])


    return str(myresult[0][0])