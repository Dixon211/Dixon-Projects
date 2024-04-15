import mediapipe as mp
import cv2

# Import necessary classes
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Define options for hand landmarker
options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='./python_test/hand_landmarker.task'),
    running_mode=VisionRunningMode.IMAGE)

# Create a hand landmarker instance using the defined options
with HandLandmarker.create_from_options(options) as landmarker:
    # The landmarker is initialized. Use it here.
    # For example, you can process an image using the landmarker:
    image_path = './image.jpg'
    image = cv2.imread(image_path)  # Read the image using OpenCV or any other library
    results = landmarker.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Process the image

    # Now you can access landmarks and other information in 'results'
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Iterate through detected hands
            for landmark in hand_landmarks.landmark:
                # Iterate through landmarks of each hand
                x = landmark.x
                y = landmark.y
                z = landmark.z  # Z-coordinate might not be available depending on the model
                # Do something with x, y, z coordinates of the landmarks
