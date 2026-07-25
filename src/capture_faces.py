import cv2
import os

print("Program Started")

def capture_face(student_id, student_name):

    # Load Haar Cascade Classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Create folder to save student's face images
    save_path = f"images/{student_id}_{student_name}"

    os.makedirs(save_path, exist_ok=True)

    # Open webcam
    camera = cv2.VideoCapture(0)
    print("Camera Opened")
    if not camera.isOpened():
        print("Camera could not be opened!")
        exit()
    print("Camera Opened Successfully")

    count = 0

    while True:

        # Read one frame from webcam
        success, frame = camera.read()
        print("Success =", success)


        if not success:
            print("Could not read frame")
            break

        # Convert image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        # Loop through detected faces
        for (x, y, w, h) in faces:

            count += 1

            # Crop face
            face = gray[y:y+h, x:x+w]

            # Save face image
            file_name = os.path.join(save_path, f"{count}.jpg")

            cv2.imwrite(file_name, face)

            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Show image count
            cv2.putText(
                frame,
                f"Images : {count}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        # Display webcam
        cv2.imshow("Capture Faces", frame)

        # Stop after 50 images or when user presses Q
        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
            break

    # Release webcam
    camera.release()

    # Close all windows
    cv2.destroyAllWindows()

    print("Face Capture Completed Successfully.")

if __name__ == "__main__":
    capture_face(1, "Jay")