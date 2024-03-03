import cv2
import mediapipe as mp

# Initialize hand detection and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    success, image = cap.read()

    # Convert image to RGB format (MediaPipe expects RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect hands in the image
    results = mp_hands.process(image_rgb)

    # Draw colored landmarks on the image
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # If hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Track the coordinates of fingertips for bounding box calculation
            wrist_x, wrist_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image.shape[1]), int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image.shape[0])
            fingertip_x = [int(landmark.x * image.shape[1]) for landmark in hand_landmarks.landmark if landmark.presence > 0.5]
            fingertip_y = [int(landmark.y * image.shape[0]) for landmark in hand_landmarks.landmark if landmark.presence > 0.5]

            # Find the minimum and maximum x and y coordinates of fingertips and wrist
            x_min, x_max, y_min, y_max = wrist_x, wrist_x, wrist_y, wrist_y
            for x in fingertip_x:
                x_min = min(x_min, x)
                x_max = max(x_max, x)
            for y in fingertip_y:
                y_min = min(y_min, y)
                y_max = max(y_max, y)

            # Draw the bounding box around the hand
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    # Draw landmarks on the hand (optional)
    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the image with bounding box and landmarks (if any)
    cv2.imshow('Hand Detection', image)

    # Exit on pressing 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
