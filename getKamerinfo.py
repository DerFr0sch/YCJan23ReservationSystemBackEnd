import mariadb
import json

def getKamerinfo(abc):
    con = mariadb.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()

    mycursor.execute("SELECT * FROM hotelkamer")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x[2])

    ab=json.dumps(myresult, indent=4, sort_keys=True, default=str)
    #ab=json.dumps( [dict(ix) for ix in myresult] )
    print(ab)
    return ab

#vanmichael()