import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)

if con:
    print("Connected")
else:
    print("Not connected")