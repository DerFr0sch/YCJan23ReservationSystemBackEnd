import mysql.connector
import json

def getMembergegevens(memberid):
    con = mysql.connector.connect(
    host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
    user="Kevindatahotel",
    password="abcd1234ABCD!@#$",
    database="hotel_database"
    )
    mycursor = con.cursor()

    mycursor.execute("SELECT * FROM member WHERE member_id="+memberid)
    myresult = mycursor.fetchall()

    jsonmemberinfo = json.dumps(myresult, indent=4, sort_keys=True, default=str)
    return jsonmemberinfo

