import cv2
import mediapipe as mp
import numpy as np
import pandas as pd

# Initialize video capture
video_path = '/Users/jenniferkim/Downloads/videoplayback.mp4'# Update this path to your video file
cap = cv2.VideoCapture(video_path)

# Initialize Mediapipe pose estimation
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Data storage for features
data = {'Frame': [], 'Arm Reach': [], 'Cadence': [], 'Objects': [], 'Area Size': []}

# Background subtractor for detecting movement/objects
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

frame_count = 0
step_times = []  # To calculate cadence based on time between steps

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    # Convert frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Pose estimation to detect arm movement
    results = pose.process(rgb_frame)
    
    arm_reach = None
    if results.pose_landmarks:
        # Calculate arm reach by measuring distance between shoulder and wrist
        shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        
        arm_reach = np.sqrt((shoulder.x - wrist.x) ** 2 + (shoulder.y - wrist.y) ** 2)

    # Detect objects using background subtraction
    fg_mask = bg_subtractor.apply(frame)
    
    # Find contours for calculating area size of moving objects
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area_size = 0
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        area_size = cv2.contourArea(largest_contour)
    
    # Cadence calculation (simplified, detecting feet movement for step timing)
    # Placeholder: You may need a more advanced method to track footfalls accurately
    if arm_reach:  # Simplified cadence based on frame count
        step_times.append(frame_count)
    
    cadence = None
    if len(step_times) > 1:
        cadence = (step_times[-1] - step_times[-2])  # Frames between steps (for illustration)

    # Store data for this frame
    data['Frame'].append(frame_count)
    data['Arm Reach'].append(arm_reach)
    data['Cadence'].append(cadence)
    data['Objects'].append(len(contours))
    data['Area Size'].append(area_size)
    
    # Display the frame for debugging (optional)
    cv2.imshow('Video Frame', frame)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Save data to CSV
df = pd.DataFrame(data)
df.to_csv('gait_features.csv', index=False)

print("Feature extraction complete. Data saved to gait_features.csv.")
