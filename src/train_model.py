import cv2
import os
import numpy as np
from PIL import Image


def train_model():

    # Create LBPH Face Recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Folder where student face images are stored
    image_path = "images"

    face_samples = []
    ids = []

    # Read each student folder
    for student_folder in os.listdir(image_path):

        folder_path = os.path.join(image_path, student_folder)

        # Skip if it is not a folder
        if not os.path.isdir(folder_path):
            continue

        # Folder name example: 101_Jay
        # Extract only the ID (101)
        student_id = int(student_folder.split("_")[0])

        # Read every image inside the student's folder
        for image_name in os.listdir(folder_path):

            image_file = os.path.join(folder_path, image_name)

            # Convert image to grayscale
            gray_image = Image.open(image_file).convert("L")

            # Convert image into NumPy array
            image_numpy = np.array(gray_image, "uint8")

            # Store image and corresponding ID
            face_samples.append(image_numpy)
            ids.append(student_id)

    print("Total Images :", len(face_samples))
    print("Student IDs :", ids)

    # Train the recognizer
    recognizer.train(face_samples, np.array(ids))

    # Create trainer folder if it doesn't exist
    os.makedirs("trainer", exist_ok=True)

    # Save the trained model
    recognizer.save("trainer/trainer.yml")

    print("Training Completed Successfully!")