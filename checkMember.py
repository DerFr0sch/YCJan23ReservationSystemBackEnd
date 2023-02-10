import mysql.connector
import json

def checkEmailadress(abc):
    con = mysql.connector.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()

    mycursor.execute("SELECT emailadress FROM hotel_database.member")

    myresult = mycursor.fetchall()

    ab=json.dumps(myresult)
    #ab=json.dumps( [dict(ix) for ix in myresult] )
    print(ab)
    return ab