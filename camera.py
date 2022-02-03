import cv2
import numpy as np
import time
import datetime

class Camera:
    """
    A Simple Wrapper for opencv's api
    It will save last 10 seconds of video in a buffer and save if and only if required
    """

    def __init__(self, size, fps=5, buffer_time=5) -> None:
        self.image_folder = "./images"
        self.width = size[0]
        self.height = size[1]
        self.fps = fps
        self.buffer_time = buffer_time
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)
        self.buffer = []
    
    def update(self):
        """
        Updates the frame
        """
        _, frame = self.cap.read()
        return frame
    
    def close(self):
        """
        Closes the camera
        """
        self.cap.release()
        cv2.destroyAllWindows()

    def save_buffer(self):
        """
        Save the all of the frames stored in buffer to a file with date and time time stamp as name
        """
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
        for index, frame in enumerate(self.buffer):
            cv2.imwrite(f"{self.image_folder}/{st}-{index}.jpg", frame)
    
    def display_window(self):
        frame = self.update()
        if self.buffer_time > 0:
            self.buffer.append(frame)
            if len(self.buffer) > self.fps * self.buffer_time:
                print("buffer full")
                self.buffer.pop(0)
            frame = self.buffer[-1]
        cv2.imshow('BIG BROTHER', frame)
        