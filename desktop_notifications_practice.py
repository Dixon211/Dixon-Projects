from plyer import notifications
import time
from datetime import datetime
import random

def show_notifications(title, message):
    notifcations.notify(title=title, message=message, timeout=10) #timeout is in seconds

def choose_message():
    

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    show_notifications("test", "hell yeah")
    time.sleep(3600)
