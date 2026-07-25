from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name



class Attendance(models.Model):
    student_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default="Present")

    def __str__(self):
        return self.student_name
    

