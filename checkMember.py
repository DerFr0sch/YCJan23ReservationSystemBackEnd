import mysql.connector
import json

def checkEmailadress(kamerid):
    con = mysql.connector.connect(
        host="hoteldatabase1.mysql.database.azure.com",  #port erbij indien mac
        user="Foxypiggyfisher",
        password="Watjewil13",
        database="hotel_database"
    )

    mycursor = con.cursor()

    sql = "SELECT emailadress FROM hotel_database.member"
    val = (kamerid,)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    ab=json.dumps(myresult)
    #ab=json.dumps( [dict(ix) for ix in myresult] )
    return ab