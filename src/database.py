import sqlite3

connection = sqlite3.connect("../database/attendance.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    student_name TEXT,
    department TEXT,
    year INTEGER
)
""")

connection.commit()

connection.close()

print("Database Created Successfully")