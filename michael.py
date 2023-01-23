import mariadb
import json

def vanmichael():
    con = mariadb.connect(
        host="localhost",  #port erbij indien mac
        user="root",
        password="",
        database="testb"
    )
    mycursor = con.cursor()

    mycursor.execute("SELECT * FROM kamer")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x[2])

    ab=json.dumps(myresult, indent=4, sort_keys=True, default=str)
    print(ab)
    return ab

#vanmichael()