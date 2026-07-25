import sqlite3

connection = sqlite3.connect("../database/attendance.db")

cursor = connection.cursor()

student_id = int(input("Enter Student ID : "))
student_name = input("Enter Student Name : ")
department = input("Department : ")
year = int(input("Year : "))

cursor.execute("""
INSERT INTO students
VALUES(?,?,?,?)
""",
(student_id,
student_name,
department,
year)
)

connection.commit()

connection.close()

print("Student Registered Successfully")