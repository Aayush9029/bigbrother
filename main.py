# Main program that runs the program, handles arguments
from cv2 import waitKey, imshow, destroyAllWindows
import coremltools
import argparse
from camera import Camera

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


if __name__ == "__main__":
    bb = BigBrother()
    bb.arguments()
    while True:
        frame = bb.big_cam.update()
        bb.big_cam.display_window()
        if waitKey(1) == 27:
            break
