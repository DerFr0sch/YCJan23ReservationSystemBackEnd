import mysql.connector
import json

def getBoekinggegevens(memberid):
    con = mysql.connector.connect(
    host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
    user="Kevindatahotel",
    password="abcd1234ABCD!@#$",
    database="hotel_database"
    )

    mycursor = con.cursor()
    mycursor.execute("SELECT * FROM boeking WHERE member_id="+memberid)
    secondresult = mycursor.fetchall()
    jsonmemberinfo = json.dumps(secondresult, indent=4, sort_keys=True, default=str)
    return jsonmemberinfo
