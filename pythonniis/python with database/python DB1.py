import sqlite3
conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("INSERT OR IGNORE INTO student VALUES(1,'Ravi',85)")
conn.commit()
conn.close()
print("Data inserted successfully")