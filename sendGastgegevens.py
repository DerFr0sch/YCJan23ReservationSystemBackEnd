import mysql.connector

def sendGastgegevensdb(voornaam, achternaam, voorvoegsel, postcode, adres, land, tel, email, betaalmethode):
    con = mysql.connector.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()

    sql = "INSERT INTO member (voornaam, achternaam, voorvoegsel, adres_straatnaam_huisnummer, adres_postcode, adres_land, telefoonnummer, emailadress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (voornaam, achternaam, voorvoegsel, adres, postcode, land, tel, email)
    mycursor.execute(sql, val)
    con.commit()

    ## HIER IS IETS MET MEMBER_ID NODIG DIE HIERBOVEN WORDT AANGEMAAKT ZODAT DE BETAALMETHODE BIJ DE JUISTE MEMBER KAN WORDEN TOEGEVOEGD
    # mycursor2 = con.cursor()
    # sql2 = "INSERT INTO boeking (betaalmethode) VALUES (%s)"
    # val2 = (betaalmethode,) 
    # mycursor2.execute(sql2, val2)  
    # con.commit()

    return "Kamer is geboekt ;)"