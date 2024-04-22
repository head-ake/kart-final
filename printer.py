class Printer:
    def __init__(self):
        # init stuff
        return

    # I'd say this will most likely be threaded, dont think that changes much for you but just a heads up
    def print(self, vals):
        # vals is list of tuples of x, y coordinates
        for val in vals:
            x, y = val
            print (x, y)

        return


