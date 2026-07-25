from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("attendance/", views.attendance, name="attendance"),
    path("students/", views.students, name="students"),

    path("attendance_report/", views.attendance_list, name="attendance_list"),


]