import cv2

def get_video_feed():
    print("\n\nOne moment the feed will start soon\n\n")
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error no feed capture, ret = False")
            break
        cv2.imshow("Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

get_video_feed()