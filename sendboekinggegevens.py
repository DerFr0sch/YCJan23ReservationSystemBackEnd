import mysql.connector
import json

def getBoekinggegevens(memberid):
    con = mysql.connector.connect(
    host="hoteldatabase1.mysql.database.azure.com",  #port erbij indien mac
    user="Foxypiggyfisher",
    password="Watjewil13",
    database="hotel_database"
    )

    mycursor = con.cursor()
    mycursor.execute("SELECT * FROM boeking INNER JOIN hotelkamer ON boeking.kamer_id = hotelkamer.kamer_id WHERE boeking.member_id="+memberid)
    secondresult = mycursor.fetchall()


    jsonmemberinfo = json.dumps(secondresult, indent=4, sort_keys=True, default=str)
    return jsonmemberinfo
