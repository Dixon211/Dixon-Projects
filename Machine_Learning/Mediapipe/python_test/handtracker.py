import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

def errorcheck(error_code):
    match error_code:
        case 0:
            return print("program closed with no errors")
        case 1:
            return print("could not capture videofeed")


def main():
    #setup for model
    model_path = "./hand_landmarker.task"
    BaseOptions = mp.tasks.BaseOptions
    HandLandmarker = mp.tasks.vision.HandLandmarker
    HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
    HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
    VisionRunningMode = mp.tasks.vision.RunningMode

    #Create handlandmarker instance in Livestream mode
    def print_result(result:HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
        print(f"hand landmarker result: {result}")
    
    options=HandLandmarkerOptions(
        base_options = BaseOptions(model_asset_path=model_path),
        running_mode = VisionRunningMode.LIVE_STREAM,
        result_callback=print_result)
    
    with


    video_cap=cv2.VideoCapture(0)

    if not video_cap.isOpened():
        return errorcheck(1)
    
    while True:
        ret , frame = video_cap.read()
        if not ret:
            errorcheck(1)
            break
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        cv2.imshow("Feed", mp_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            errorcheck(0)
            break

    video_cap.release()
    cv2.destroyAllWindows()




if __name__ == "__main__":
    main()