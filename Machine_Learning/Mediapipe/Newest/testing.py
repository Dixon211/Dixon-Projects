import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results=hands.process(image)
    if results.multi_hand_landmarks:
        primaryhand = results.multi_hand_landmarks[0]
        print(primaryhand)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break