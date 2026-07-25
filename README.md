# 🎯 Face Recognition Attendance System

A web-based attendance management system built with **Django** and **OpenCV** that automates attendance marking using real-time face recognition through a webcam — eliminating the need for manual roll calls.

---

## 📌 Project Objective

The Face Recognition Attendance System automates student attendance by detecting and recognizing faces via webcam, matching them against a trained model, and logging attendance directly into a database — reducing manual effort and proxy attendance.

---

## 🛠️ Technologies Used

| Category | Tech Stack |
|---|---|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python, Django |
| **Database** | SQLite |
| **Libraries** | OpenCV, NumPy, Pillow |
| **Machine Learning** | LBPH (Local Binary Pattern Histogram) Face Recognizer, Haar Cascade Face Detection |

---

## 🧩 Project Modules

### 1. Home Page
Dashboard with quick access to:
- Register Student
- Take Attendance
- View Students
- Attendance Report

### 2. Student Registration
Admin enters student details (ID, Name, Department, Year) →  
Details saved to database → Webcam opens → 50 face images captured → Model trained automatically → Registration complete.

### 3. Face Capture (`capture_faces.py`)
Opens webcam → detects face → crops → saves 50 grayscale images per student into:
