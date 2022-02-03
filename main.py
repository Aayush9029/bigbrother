# Main program that runs the program, handles arguments
from cv2 import waitKey, imshow, destroyAllWindows
import coremltools as ct
import argparse

from sympy import true
from camera import Camera
from lid import is_lid_closed
from time import sleep
import threading
import multiprocessing
from PIL import Image

class BigBrother:
    """
    Parses arguments and runs the program
    """
    def __init__(self):
        # Set the size of the camera and initialize the camera
        self.big_cam = Camera((640, 480))
        # Play noise
        self.scream = False
        # Send message via webhook
        self.notify = True
        # Logging
        self.verbose = True
        # Displays a barcode that leads to repo, and a DO NOT TOUCH message
        self.display_code = False 
        # Use this password to disengage the alarm system
        self.passcode = "12345"

        # sepecifying the model
        self.model = ct.models.MLModel('model/bigbrother.mlmodel')

    def arguments(self):
        """
        Parses arguments and sets flags
        """
        parser = argparse.ArgumentParser(description="Runs the alarm system")
        parser.add_argument("--no-noise", help="Turns off the alarm noise", action="store_false")
        parser.add_argument("--no-notify", help="Turns off the webhook notification", action="store_false")
        parser.add_argument("--no-log", help="Turns off the logging", action="store_false")
        parser.add_argument("--no-display", help="Turns off the display", action="store_false")
        parser.add_argument("--passcode", help="Sets the passcode", default=self.passcode)
        args = parser.parse_args()
        self.scream = args.no_noise
        self.notify = args.no_notify
        self.verbose = args.no_log
        self.display_code = args.no_display
        self.passcode = args.passcode

    def check_intruder(self, frame):

        # convert frame to PIL image
        img = Image.fromarray(frame)
        # convert to coreml format

        return self.model.predict({'image': img })['classLabel']

    def main(self):
        frame_count = 0
        while True:
            frame_count += 1
            print(frame_count, end="\r")
            self.big_cam.display_window()
            if waitKey(1) == 27:
                self.big_cam.save_buffer()
                break
            
            if frame_count % 30 == 0:
                result = self.check_intruder(self.big_cam.update())
                print(result)
                if result == "Intruder":
                    self.big_cam.save_buffer()
                    exit()
#                     TODO: Upload to github, and cool stuff or something to alert myself and the intruder

            # Check if the lid is closed
            if is_lid_closed():
                # save the frame
                self.big_cam.save_buffer()



if __name__ == "__main__":
    bb = BigBrother()
    bb.arguments()
    bb.main()

