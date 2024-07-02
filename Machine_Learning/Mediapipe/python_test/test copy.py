import cv2
import mediapipe as mp
import json



def unpack_landmarks(results, frame):
    ML_positions = {}
    for j, hand_landmarks in enumerate(results.multi_hand_landmarks):
        for i, handlandmark in enumerate(hand_landmarks.landmark):
            match i:
                case 4:
                    x,y,z= int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0]), int(landmark.z)
                    cv2.circle(frame,(x, y), 5, (255,0,0), -1)
                    ML_positions[f"Thumb {j}"] = [x, y, z]
                case 8:
                    x,y,z= int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0]), int(landmark.z)
                    cv2.circle(frame,(x, y), 5, (255,0,0), -1)
                    ML_positions[f"Pointer {j}"] = [x, y, z]
                case 12:
                    x,y,z= int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0]), int(landmark.z)
                    cv2.circle(frame,(x, y), 5, (255,0,0), -1)
                    ML_positions[f"Middle {j}"] = [x, y, z]
                case 16:
                    x,y,z= int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0]), int(landmark.z)
                    cv2.circle(frame,(x, y), 5, (255,0,0), -1)
                    ML_positions[f"Ring {j}"] = [x, y, z]
                case 20:
                    x,y,z= int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0]), int(landmark.z)
                    cv2.circle(frame,(x, y), 5, (255,0,0), -1)
                    ML_positions[f"Pinky {j}"] = [x, y, z]
    return(ML_positions)
        
def check_position(marklist):

    return 0


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)

#Main            
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results=hands.process(image)
    #process to put circles on the image and what color they are
    if results.multi_hand_landmarks:
        #print(unpack_landmarks(results.multi_hand_landmarks))
        for hand_landmarks in results.multi_hand_landmarks:
            for i, landmark in enumerate(hand_landmarks.landmark):
                x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), int(landmark.z)
                #switch statement checks for tip of thumb[4], tip of pointer[8], and tip of middle finger[12]
                match i:
                    case 8 | 4 | 12 | 16 | 20:
                        cv2.circle(frame, (x,y), 5, (255,0,0), -1)
                    case _:
                        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)                   
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()