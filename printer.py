import serial # pip install serial
import time
from mecode import G
import threading

class Printer:
    WRITE = 0
    MOVE = 15
    PORT = "COM3"  # to get port run python -m serial.tools.list_ports
    baud = 115200
    home = "G28"
    SIZE = 15
    center_cmd = "G1 X110 Y110 Z20 F3000\n"
    lock = threading.Lock()

    @staticmethod
    def remove_object_str(gcode_string):
        index = gcode_string.find("<mecode.main.G object")
        if index != -1:
            gcode_string = gcode_string[:index]
        return gcode_string

    @staticmethod
    def cross(point, size):
        g = G()
        g.abs_move(point[0] - size, point[1] - size, Printer.MOVE)
        g.abs_move(point[0] - size, point[1] - size, Printer.WRITE)
        g.abs_move(point[0] + size, point[1] + size, Printer.WRITE)
        g.abs_move(point[0] + size, point[1] + size, Printer.MOVE)
        g.abs_move(point[0] - size, point[1] + size, Printer.MOVE)
        g.abs_move(point[0] - size, point[1] + size, Printer.WRITE)
        g.abs_move(point[0] + size, point[1] - size, Printer.WRITE)
        g.abs_move(point[0] - size, point[1] - size, Printer.MOVE)
        gcode = Printer.remove_object_str(str(g))
        return gcode

    def send_gcode(self, gcode):
        self.cereal.write(gcode.encode('utf-8'))
        time.sleep(1)

    def send_gcode_lines(self, gcode_string):
        lines = gcode_string.split('\n')
        for line in lines:
            print("Sending line")
            self.send_gcode(line)
            time.sleep(2)  

    def __init__(self):
        # init stuff
        self.cereal = serial.Serial(self.PORT, self.baud, timeout=1)
        self.send_gcode(self.center_cmd)

    # I'd say this will most likely be threaded, don't think that changes much for you but just a heads up
    def print(self, vals):
        # vals is a list of tuples of x, y coordinates
        for val in vals:
            x, y = val
            # sleep for 3 secs to simulate the drawing process
            # self.lock.acquire()
            self.send_gcode_lines((Printer.cross(val, Printer.SIZE)))
            # self.lock.release() 
            #time.sleep(30)
            print(x, y)
        self.send_gcode(self.center_cmd)

    # Call close when to close the serial port
    def close(self):
        self.send_gcode(self.home)
        self.cereal.close()

if __name__ == "__main__":
    printer = Printer()
    printer.print([(50, 50), (75, 50)])
    printer.close()