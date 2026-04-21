import sqlite3

conn = sqlite3.connect("student.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Use INSERT OR IGNORE to avoid duplicate error
cur.execute("INSERT OR IGNORE INTO student VALUES(1,'Ravi',85)")

conn.commit()
conn.close()

print("Data inserted successfully")
