import mysql.connector

def sendKamerreservering(kamerid):
    con = mysql.connector.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()

    sql = "UPDATE hotelkamer SET reservering = 1 WHERE kamer_id = %s"
    val = (kamerid,)
    mycursor.execute(sql, val)
    #print(val,flush=True)
    con.commit()
    print(mycursor.rowcount, "Kamer gereserveerd")
    return "gereserveerd"

#sendKamerinfo("test1")
