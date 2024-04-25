import time

class Printer:
    def __init__(self):
        # init stuff
        return

    # I'd say this will most likely be threaded, dont think that changes much for you but just a heads up
    def print(self, vals):
        # vals is list of tuples of x, y coordinates
        for val in vals:
            x, y = val
            # sleep for 3 secs to simulate drawing process
            time.sleep(3)
            print (x, y)

        return

if __name__ == "__main__":
    printer = Printer()
    printer.print([(1, 2), (3, 4)])
