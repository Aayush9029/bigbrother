import cv2
import numpy as np
import time


class Camera:
    """
    A Simple Wrapper for opencv's api
    """

    def __init__(self, size, fps=30) -> None:
        self.width = size[0]
        self.height = size[1]
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)
    

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
    
    def display_window(self):
        frame = self.update()
        cv2.imshow('BIG BROTHER', frame)
        