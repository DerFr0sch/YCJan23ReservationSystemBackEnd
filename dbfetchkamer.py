import mysql.connector
import json

def getSpecifickamer(kamerid):
    con = mysql.connector.connect(
        host="hoteldatabase1.mysql.database.azure.com",  #port erbij indien mac
        user="Foxypiggyfisher",
        password="Watjewil13",
        database="hotel_database"
    )

    mycursor = con.cursor()

    sql = "SELECT * FROM hotelkamer WHERE kamer_id = %s"
    val = (kamerid,)
    
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()
    print(myresult)
    ab=json.dumps(myresult)
    #ab=json.dumps( [dict(ix) for ix in myresult] )
    print(ab)

    return ab
