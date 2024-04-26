from mecode import G

class Pooper:
    WRITE = 0
    MOVE = 15
    PORT = "COM3"  # to get port run python -m serial.tools.list_ports
    baud = 115200
    home = "G28"
    SIZE = 15
    center_cmd = "G1 X110 Y110 Z20 F3000\n"

    def cross(self, point, size):
        self.g.abs_move(point[0] - size, point[1] - size, Printer.MOVE)
        self.g.abs_move(point[0] - size, point[1] - size, Printer.WRITE)
        self.g.abs_move(point[0] + size, point[1] + size, Printer.WRITE)
        self.g.abs_move(point[0] + size, point[1] + size, Printer.MOVE)
        self.g.abs_move(point[0] - size, point[1] + size, Printer.MOVE)
        self.g.abs_move(point[0] - size, point[1] + size, Printer.WRITE)
        self.g.abs_move(point[0] + size, point[1] - size, Printer.WRITE)
        self.g.abs_move(point[0] - size, point[1] - size, Printer.MOVE)


    def __init__(self):
        # init stuff
        self.g = G(
            direct_write=True,
            direct_write_mode="serial",
            printer_port=self.PORT,
            baudrate=self.baud
        )

        self.g.write(self.center_cmd)

    def print(self, vals):
        for val in vals:
            x, y = val
            print(x, y)
            self.cross(val, self.SIZE)
        self.g.write("M400")

    def close(self):
        self.g.write(self.home)
        self.g.write("M400")
        self.g.teardown()

if __name__ == "__main__":
    printer = Pooper()
    printer.print([(50, 50), (75, 50)])
    printer.close()
