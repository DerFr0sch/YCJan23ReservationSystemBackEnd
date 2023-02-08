import mysql.connector

def sendKamerboeking(kamerid):
    con = mysql.connector.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()
    
    sql = "UPDATE hotelkamer SET boeking = 1 WHERE kamer_id = %s"
    val = (kamerid,)
    mycursor.execute(sql, val)

    #print(val,flush=True)
    
    con.commit()
    print(mycursor.rowcount, "Kamer geboekt")
    return "geboekt"

#sendKamerinfo("test1")
