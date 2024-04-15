import cv2
import mediapipe as mp
import json

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results=hands.process(image)

    def unpack_landmarks(results):
        landmark_data = []
        for hand_landmarks in results:
            for i, handlandmark in enumerate(hand_landmarks.landmark):
                data = handlandmark
                return(data)



    #process to put circles on the image and what color they are
    if results.multi_hand_landmarks:
        print(unpack_landmarks(results.multi_hand_landmarks))
        for hand_landmarks in results.multi_hand_landmarks:
            for i, landmark in enumerate(hand_landmarks.landmark):
                x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), int(landmark.z)
                #switch statement checks for tip of thumb[4], tip of pointer[8], and tip of middle finger[12]
                match i:
                    case 8 | 4 | 12:
                        cv2.circle(frame, (x,y), 5, (255,0,0), -1)

                    case _:
                        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()