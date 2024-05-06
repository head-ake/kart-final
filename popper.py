import serial # pip install serial
import time
from mecode import G
import gcode

class Popper:
    WRITE = 0
    MOVE = 15
    PORT = "/dev/cu.usbserial-1430"  # to get port run python -m serial.tools.list_ports
    baud = 115200
    home = "G28"
    SIZE = 15
    center_cmd = "G1 X110 Y110 Z20 F3000\n"

    def __init__(self):
        SIZE = 10

    # I'd say this will most likely be threaded, don't think that changes much for you but just a heads up
    def print(self, vals):
        gcode.getGCode(True, vals)
        gcode.outputFile()

    # Call close when to close the serial port
    def close(self):
        SIZE = 10

if __name__ == "__main__":
    printer = Popper()
    printer.print([(0, 0), (200, 200), (0, 200), (25, 25)])
    time.sleep(30)
    # printer.close()
