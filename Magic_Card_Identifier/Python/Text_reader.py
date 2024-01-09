import cv2
import numpy as np
import matplotlib as mpl
import easyocr

#image + properties
image_path = "./Python/235956.webp"
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (1, 1), 0)
height, width, _ = img.shape
ret, thresh = cv2.threshold(blurred, 120, 255, cv2.ADAPTIVE_THRESH_MEAN_C)

#reader object from easyocr
reader = easyocr.Reader(['en'])
image_text = reader.readtext(thresh, detail=1)
#print(image_text)

cord_info, card_name, accuracy = image_text[0]
#print(image_text[0])
name_box = cv2.rectangle(img, cord_info[0], cord_info[2], (0,0,255), 3)

#print(f"height = {height}\n width = {width}")

# start, stop, color, thickness
line = cv2.line(thresh, (1, (height//2)), (width, (height//2)), (0, 255, 0), 2)
cv2.imshow("box", img)
cv2.waitKey(0)