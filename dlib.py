import dlib
import cv2
import face_recognition

# Load image
image_path = "student_faces/1001.jpg"  # Change this to test other images
image = cv2.imread(image_path)

if image is None:
    print("❌ Error: Image not found or invalid format.")
else:
    # Convert image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect face locations
    face_locations = face_recognition.face_locations(rgb_image)

    if len(face_locations) == 0:
        print("❌ No face detected in the image.")
    else:
        print(f"✅ Detected {len(face_locations)} face(s) in {image_path}")

        # Extract face encodings
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        if len(face_encodings) > 0:
            print("✅ Face encoding generated successfully!")
        else:
            print("❌ Error: Face detected but encoding failed.")
import dlib
import cv2
import face_recognition

# Load image
image_path = "student_faces/1001.jpg"  # Change this to test other images
image = cv2.imread(image_path)

if image is None:
    print("❌ Error: Image not found or invalid format.")
else:
    # Convert image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect face locations
    face_locations = face_recognition.face_locations(rgb_image)

    if len(face_locations) == 0:
        print("❌ No face detected in the image.")
    else:
        print(f"✅ Detected {len(face_locations)} face(s) in {image_path}")

        # Extract face encodings
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        if len(face_encodings) > 0:
            print("✅ Face encoding generated successfully!")
        else:
            print("❌ Error: Face detected but encoding failed.")
