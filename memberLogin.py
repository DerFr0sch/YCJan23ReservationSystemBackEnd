import json
import mysql.connector

def login(userEmail, userPassword):

    loginState = "false"

    con = mysql.connector.connect(
        host="ycjanhoteldatabase.mysql.database.azure.com",  #port erbij indien mac
        user="Kevindatahotel",
        password="abcd1234ABCD!@#$",
        database="hotel_database"
    )

    mycursor = con.cursor()


    getStoredemail = "SELECT emailadress FROM hotel_database.member WHERE emailadress = %s"
    val = (userEmail,)    

    mycursor.execute(getStoredemail, val)

    storedEmail = mycursor.fetchall()

    getStoredwachtwoord = "SELECT wachtwoord FROM hotel_database.member WHERE emailadress = %s"
    val2 = (userEmail,)    

    mycursor.execute(getStoredwachtwoord, val2)

    storedPassword = mycursor.fetchall()

    # auth = userPassword.encode()
    # auth_hash = hashlib.md5(auth).hexdigest()

    if storedEmail[0][0] == userEmail and storedPassword[0][0] == userPassword:
        print("Succesvol ingelogd!")

        getUserid = "SELECT member_id FROM hotel_database.member WHERE emailadress = %s"
        val = (userEmail,)    

        mycursor.execute(getUserid, val)
        loginState = str(mycursor.fetchall()[0][0])
        print(loginState)

    else:
        print("E-mail of wachtwoord onjuist.")
    
    print(loginState)
    return loginState