# pro1.py
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="40Abhishek",
        password="Jenna@40",
        database="teacher"
    )

    cursor = con.cursor()

    cursor.execute("SELECT * FROM instructor;")
    result = cursor.fetchall()

    for row in result:
        print(row)

    con.close()

except mysql.connector.Error as err:
    print("Error:", err)
