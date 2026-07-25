from django.shortcuts import render
from .models import Student
import sys
import os

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "src"))

from src.capture_faces import capture_face
from src.train_model import train_model
from src.recognize_faces import recognize_faces


def home(request):
    return render(request, "home.html")


def register(request):

    if request.method == "POST":

        student_id = request.POST.get("student_id")
        name = request.POST.get("student_name")
        department = request.POST.get("department")
        year = request.POST.get("year")

         # Check if Student ID already exists
        if Student.objects.filter(student_id=student_id).exists():

            return render(request, "register.html", {
                "error": "Student ID already exists!"
            })

        # Save student details in database
        student = Student(
            student_id=student_id,
            name=name,
            department=department,
            year=year
        )
        student.save()

        # Capture face
        capture_face(student_id, name)

        # Train model
        train_model()

        return render(request, "home.html", {
            "message": "Student Registered and Face Captured Successfully!"
        })

    return render(request, "register.html")


def attendance(request):

    recognize_faces()

    return render(request, "home.html", {
        "message": "Attendance Marked Successfully!"
    })

from .models import Student, Attendance

def students(request):
    students = Student.objects.all()

    return render(request, "students.html", {
        "students": students
    })


def attendance_list(request):
    attendance = Attendance.objects.all()

    return render(request, "attendance_list.html", {
        "attendance": attendance
    })