import multiprocessing as mp
import cv2
import sys

def grayscale_view(video_feed, queue):
        rval, frame = video_feed.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        queue.put(gray)
        print(queue)



if __name__=="__main__":
    frame_queue = mp.Queue()
    vc = cv2.VideoCapture(0)

    while True:
        camera_feed = mp.Process(target=grayscale_view, args=(vc, frame_queue,))
        camera_feed.start()
        camera_feed.join()
        print("starting camera feed")

