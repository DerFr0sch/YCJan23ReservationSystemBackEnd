import mysql.connector

def sendKamerboeking(kamerid, totprijs, boeking_begin, boeking_eind, betaalmet):
    con = mysql.connector.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()
    
    sql = "INSERT INTO boeking (kamer_id, totaalprijs, boekingsdatum_begin, boekingsdatum_eind, betaalmethode) VALUES (%s, %s, %s, %s, %s)"
    val = (kamerid, totprijs, boeking_begin, boeking_eind, betaalmet)
    print(val)
    mycursor.execute(sql, val)

    con.commit()
    return "geboekt"
