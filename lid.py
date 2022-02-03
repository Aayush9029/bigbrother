# Program that tells if the the laptios lid is open or closed

from os import popen


def is_lid_closed():
    command = "ioreg -r -k AppleClamshellState -d 4 | grep AppleClamshellState  | head -1 | awk '{print $4}'"
    output = popen(command).read().strip()
    if output == "0x0\n" or output == "Yes":
        return True
    else:
        return False