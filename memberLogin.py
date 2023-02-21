import hashlib
import json
import mysql.connector

#https://yc2301hotelbackend.azurewebsites.net

def login(userEmail, userPassword):

    loginState = False

    con = mysql.connector.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()

    storedEmail = mycursor.execute("SELECT emailadress FROM hotel_database.member")
    storedPassword = mycursor.execute("SELECT wachtwoord FROM hotel_database.member")

    # auth = userPassword.encode()
    # auth_hash = hashlib.md5(auth).hexdigest()

    print("user email = "+userEmail)
    print("user password = "+userPassword)
    print("stored email = "+storedEmail)
    print("stored password = "+storedPassword)

    if storedEmail == userEmail and storedPassword == userPassword:
        print("Succesvol ingelogd!")
        loginState = True
    
    else:
        print("E-mail of wachtwoord onjuist.")
    
    return loginState