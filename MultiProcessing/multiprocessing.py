import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MARGIN = 10
ROW_SIZE= 10
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)

def visualize(image, detection_result) -> np.ndarray:
        for detection in detection_result.detections:
                bbox = detection.bounding_box
                start_point = bbox.origin_x, bbox.origin_y + bbox.height
                cv2.rectangle(image, start_point, end_point, TEXT_COLOR, 3)

                category = detection.categories[0]
                category_name = category.category_name
                probability = round(category.score, 2)
                result_text = category_name + f'({probability})'
                text_location = (MARGIN + bbox.origin_x, MARGIN + ROW_SIZE + bbox.origin_y)
                cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN, FONT_SIZE, TEXT_COLOR, FONT_THICKNESS)

        return image

img_file = "me.jpg"
img=cv2.imread(img_file)
cv2.imshow(img)

