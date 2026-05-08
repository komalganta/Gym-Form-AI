import cv2
import mediapipe as mp
from geometry import PoseGeometry

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

print("System Active. Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    # Convert to RGB for MediaPipe processing
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.pose_landmarks:
        # Draw the visual skeleton
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        landmarks = results.pose_landmarks.landmark
        
        try:
            # Extract Right Side: Shoulder(12), Elbow(14), Wrist(16), Hip(24)
            shoulder = [landmarks[12].x, landmarks[12].y, landmarks[12].z]
            elbow = [landmarks[14].x, landmarks[14].y, landmarks[14].z]
            wrist = [landmarks[16].x, landmarks[16].y, landmarks[16].z]
            hip = [landmarks[24].x, landmarks[24].y, landmarks[24].z]

            # Logic: Calculate the Curl and the Swing
            curl_angle = PoseGeometry.calculate_angle(shoulder, elbow, wrist)
            swing_angle = PoseGeometry.calculate_angle(shoulder, elbow, hip)

            # Visual Feedback
            color = (0, 255, 0) if swing_angle < 15 else (0, 0, 255)
            cv2.putText(image, f"CURL: {int(curl_angle)}", (10, 30), 1, 1.5, (255, 255, 255), 2)
            cv2.putText(image, f"SWING: {int(swing_angle)}", (10, 70), 1, 1.5, color, 2)

            if swing_angle > 15:
                cv2.putText(image, "STOP SWINGING!", (10, 110), 1, 1.5, (0, 0, 255), 2)

        except Exception as e:
            pass

    cv2.imshow('Gym Form AI Backend', image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()