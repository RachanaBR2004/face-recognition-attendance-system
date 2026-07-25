import sqlite3

connection = sqlite3.connect("../database/attendance.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()