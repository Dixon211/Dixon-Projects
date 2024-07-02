
from time import sleep
import math
import threading
import clicknium as cc
import keyboard

# Function to perform circular mouse movement
def circle():
    a, b = cc.mouse.position()
    w = 20  
    m = (2 * math.pi) / w 
    r = 200      

    print("Press 'q' to stop the script.")
    
    # Function to monitor key press
    def check_key_press():
        while True:
            if keyboard.is_pressed('q'):
                print("You pressed 'q'. Stopping the script.")
                global running
                running = False
                return

    # Start a thread to monitor key presses
    key_thread = threading.Thread(target=check_key_press)
    key_thread.start()

    global running
    running = True

    while running:
        for i in range(0, w + 1):
            if not running:
                break
            x = int(a + r * math.sin(m * i))  
            y = int(b + r * math.cos(m * i))
            cc.mouse.move(x, y)
            sleep(0.2)

if __name__ == "__main__":
    circle()