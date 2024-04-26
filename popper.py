import serial # pip install serial
import time
from mecode import G
import gcode

class Popper:
    WRITE = 0
    MOVE = 15
    PORT = "COM3"  # to get port run python -m serial.tools.list_ports
    baud = 115200
    home = "G28"
    SIZE = 15
    center_cmd = "G1 X110 Y110 Z20 F3000\n"
    
    def cross(self, point, size):
        self.g.abs_move(point[0] - size, point[1] - size, Popper.MOVE)
        self.g.abs_move(point[0] - size, point[1] - size, Popper.WRITE)
        self.g.abs_move(point[0] + size, point[1] + size, Popper.WRITE)
        self.g.abs_move(point[0] + size, point[1] + size, Popper.MOVE)
        self.g.abs_move(point[0] - size, point[1] + size, Popper.MOVE)
        self.g.abs_move(point[0] - size, point[1] + size, Popper.WRITE)
        self.g.abs_move(point[0] + size, point[1] - size, Popper.WRITE)
        self.g.abs_move(point[0] + size, point[1] - size, Popper.MOVE)
    
    def dot(self, point, size):
        self.g.abs_move(point[0], point[1], Popper.MOVE)
        self.g.abs_move(point[0], point[1], Popper.WRITE)
        self.g.abs_move(point[0], point[1], Popper.MOVE)


    def send_gcode(self, gcode):
        self.cereal.write(gcode.encode('utf-8'))
        time.sleep(1)

    def __init__(self):
        SIZE = 10
        # init stuff
        # self.g = G(outfile=r'D:/Turner-Barbour/kart-final/file.gcode')
        # self.cereal = serial.Serial(self.PORT, self.baud, timeout=1)

    # I'd say this will most likely be threaded, don't think that changes much for you but just a heads up
    def print(self, vals):
        gcode.getGCode(True, vals)
        gcode.outputFile()
        # vals is a list of tuples of x, y coordinates
        for val in vals:
            x, y = val
            # self.cross(val, self.SIZE)

    # Call close when to close the serial port
    def close(self):
        SIZE = 10
        # self.g.teardown()
        # self.cereal.close()
    
    # def outputFile(self):
    #     file = open('D:/Turner-Barbour/kart-final/file.gcode', 'r')
    #     with open('D:/Turner-Barbour/kart-final/file.gcode', 'r') as f:
    #         print(f.read())
    #         for line in f:
    #             print(line)

if __name__ == "__main__":
    printer = Popper()
    printer.print([(25, 25), (25, 25), (25, 25), (25, 25),(25, 25)])
    time.sleep(30)
    printer.print([(15, 15), (75, 75)])
    # printer.close()
