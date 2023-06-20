import os
import cv2
import dlib

def detect_faces(video_path):
    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the pre-trained face recognition model
    face_detector = dlib.get_frontal_face_detector()

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        return

    # Create the "faces" directory if it doesn't exist
    output_dir = "faces"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frame_count = 0

    while cap.isOpened():
        # Read the current frame
        ret, frame = cap.read()

        # Break the loop if the video has ended
        if not ret:
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Reduce the frame size for faster processing (optional)
        small_gray = cv2.resize(gray, (0, 0), fx=0.5, fy=0.5)

        # Detect faces in the current frame
        faces = face_cascade.detectMultiScale(small_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Process each detected face
        for (x, y, w, h) in faces:
            # Scale the coordinates back to the original frame size
            x *= 2
            y *= 2
            w *= 2
            h *= 2

            # Verify if the detected region contains a valid face using the face recognition model
            face_region = frame[y:y+h, x:x+w]
            dlib_rect = dlib.rectangle(x, y, x+w, y+h)
            detected_faces = face_detector(face_region, 1)
            
            # Save the face image only if a valid face is detected
            if len(detected_faces) == 1:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Save each face as a separate image
                face_img = frame[y:y+h, x:x+w]
                output_path = os.path.join(output_dir, f"face_{frame_count}.jpg")
                cv2.imwrite(output_path, face_img)
                frame_count += 1

    # Release the video capture
    cap.release()

if __name__ == '__main__':
    video_path = ''  # Replace with your video file path
    detect_faces(video_path)

