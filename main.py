# Main program that runs the program, handles arguments

import os
import cv2
import numpy as np
import coremltools
import argparse


class BigBrother:
    """
    Parses arguments and runs the program
    """
    def __init__(self):
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

        self.size = {
            "width": 720,
            "height": 480
        }

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
    
    def main(self):
        cap = cv2.VideoCapture(0)
        # Set camera resolution. The max resolution is webcam dependent
        # so change it to a resolution that is both supported by your camera
        # and compatible with your monitor  
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.size["width"])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.size["height"])

        # If you have problems running this code on MacOS X you probably have to reinstall opencv with
        # qt backend because cocoa support seems to be broken:
        #   brew reinstall opencv --HEAD --qith-qt



        while True:
            ret, frame = cap.read()
            cv2.imshow('BIG BROTHER', frame)
            # 27 is the escape key for macbook not sure if it works on other systems :)
            if cv2.waitKey(1) == 27:
                break

        cap.release()
        cv2.destroyAllWindows()


    def watch(self):
        """
        Runs the program
        """
        # Get the arguments
        self.arguments()
        # Run the program
        self.main()




if __name__ == "__main__":
    cap = cv2.VideoCapture(0) 
    # Create the object
    bb = BigBrother()
    # Run the program
    bb.watch()
    # Release the camera
    cap.release()
    # Destroy all windows
    cv2.destroyAllWindows()