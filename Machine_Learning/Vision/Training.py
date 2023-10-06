from PIL import Image
import cv2
import time

def take_picture(ret, path, frame):
    if ret:
        cv2.imwrite(path, frame)
    else:
        print("Error: Could not capture image")

def create_user():
    print("what is your name?")
    name = input()
    print("\n Thank you, We will need to scan you for use of this program.\n")
    print("\nI am going to take some sample images. Please press \"1\" when you are ready\n")
    wait = input()
    print("\none moment, we will take a picture soon\n")


    cv2.namedWindow("Scan")
    vc=cv2.VideoCapture(0)
    if not vc.isOpened():
        print("\nError: Could not open camera.\n")
#countdown
    x=3
    while x>0:
        print(x)
        time.sleep(1)
        x = x-1

    ret, frame = vc.read()
    path = (f"./Training/{name}.jpg")
    take_picture(ret, path, frame)
    
    pic = Image.open(path)
    pic.show()
    print("\n Is this an ok picture? (Y/N)\n")
    ans = input()
    if ans.lower() == "y":
        print("Thank you")
        pic.close()
        return path
    else:
        pic.close()
        print("Let's try again")
        take_picture(ret,name,frame)



create_user()
