import cv2
import os
import sys
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "face_system.settings"
)

import django
django.setup()

from attendance_app.models import Student, Attendance


def recognize_faces():

    # Load trained model
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read(
        os.path.join(BASE_DIR, "trainer", "trainer.yml")
    )

    # Load face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    camera = cv2.VideoCapture(0)


    while True:

        success, frame = camera.read()

        if not success:
            break


        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )


        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5
        )


        for (x, y, w, h) in faces:

            face = gray[y:y+h, x:x+w]


            predicted_id, confidence = recognizer.predict(face)


            print("Predicted ID :", predicted_id)
            print("Confidence   :", confidence)



            if confidence < 70:


                # Fix for 1 and 01 mismatch
                student = Student.objects.filter(
                    student_id__in=[
                        str(predicted_id),
                        str(predicted_id).zfill(2)
                    ]
                ).first()


                print("Student Found :", student)



                if student:


                    already_marked = Attendance.objects.filter(
                        student_id=student.student_id,
                        date=date.today()
                    ).exists()



                    if not already_marked:


                        Attendance.objects.create(
                            student_id=student.student_id,
                            student_name=student.name,
                            status="Present"
                        )


                        message = "Attendance Marked"


                    else:

                        message = "Already Marked"



                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x+w, y+h),
                        (0,255,0),
                        2
                    )


                    cv2.putText(
                        frame,
                        student.name,
                        (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0,255,0),
                        2
                    )


                    cv2.putText(
                        frame,
                        message,
                        (20,40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255,0,0),
                        2
                    )



                    # Close camera after successful marking
                    if message == "Attendance Marked":

                        cv2.imshow(
                            "Attendance",
                            frame
                        )

                        cv2.waitKey(1500)

                        camera.release()
                        cv2.destroyAllWindows()

                        return



                else:


                    cv2.putText(
                        frame,
                        "Student Not Found",
                        (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0,0,255),
                        2
                    )



            else:


                cv2.putText(
                    frame,
                    "Unknown Face",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,0,255),
                    2
                )



            cv2.rectangle(
                frame,
                (x,y),
                (x+w,y+h),
                (0,255,0),
                2
            )



        cv2.imshow(
            "Attendance",
            frame
        )



        # Press Q to exit manually
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break



    camera.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    recognize_faces()