import cv2
import numpy as np
import face_recognition
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ============ MySQL Connection ============
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # Change if your MySQL username is different
    password="nasa@20012006",  # Change to your MySQL password
    database="attendancereg"  # Ensure this database exists in MySQL
)
cursor = conn.cursor()

# ============ Load Known Faces from Three Specific Image Paths ============
known_face_encodings = []
known_face_names = []

# Manually define three images
students = {
    "5084": "C:/Users/Naren Sai A/Pictures/Camera Roll/1001.jpg",
    "5083": "C:/Users/Naren Sai A/Pictures/Camera Roll/1002.jpg",
    "5111": "C:/Users/Naren Sai A/Pictures/Camera Roll/1003.jpg"
}

for student_id, img_path in students.items():
    image = cv2.imread(img_path)

    if image is None:
        print(f"❌ Error: Image {img_path} not found.")
        continue  # Skip this student

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_image)

    if len(face_locations) == 0:
        print(f"❌ No face detected in {img_path}")
        continue  # Skip if no face found

    face_encoding = face_recognition.face_encodings(rgb_image, face_locations)[0]
    known_face_encodings.append(face_encoding)
    known_face_names.append(student_id)

print("✅ All student faces loaded successfully!")

# ============ Face Recognition Function ============
def recognize_face():
    cap = cv2.VideoCapture(0)  # Open webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error: Camera not working")
            break

        rgb_small = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small)

        if len(face_locations) == 0:
            print("❌ No face detected.")
            continue

        face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"

            if True in matches:
                matched_idx = matches.index(True)
                name = known_face_names[matched_idx]

                # Insert into MySQL database (attendance table must have 'reg_no' & 'name')
                cursor.execute(
                    "INSERT INTO attendance (reg_no, name) VALUES (%s, %s)",
                    (name, "Student " + name)
                )
                conn.commit()  # Save changes

                messagebox.showinfo("Attendance", f"✅ Attendance marked for Student {name}")

        cap.release()
        cv2.destroyAllWindows()
        break

# ============ Enhanced Tkinter GUI ============
root = tk.Tk()
root.title("🎓 Student Attendance System")
root.geometry("400x300")  # Window size
root.configure(bg="#f2f2f2")  # Background color

# Title Label
title_label = ttk.Label(
    root,
    text="📸 Face Recognition Attendance",
    font=("Helvetica", 14, "bold"),
    background="#f2f2f2",
    foreground="#333"
)
title_label.pack(pady=20)

# Recognize Face Button
btn_recognize = ttk.Button(
    root,
    text="📷 Recognize Face & Mark Attendance",
    command=recognize_face,
    style="TButton"
)
btn_recognize.pack(pady=10)

# Exit Button
btn_exit = ttk.Button(
    root,
    text="❌ Exit",
    command=root.quit,
    style="TButton"
)
btn_exit.pack(pady=10)

# Apply styles to buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)

# Run GUI
root.mainloop()

