from mecode import G
import serial

printer_port = 'COM3'
baud = 115200
# cereal = serial.Serial(printer_port, baud, timeout=1)
home = "G28"

outfile_path = 'file.gcode'

def getGCode(toFile: bool, list):
    WRITINGDEPTH = 0
    MOVINGDEPTH = 15
    g = G(outfile=outfile_path)

    def circle(point, size):
        g.abs_move(point[0]-size, point[1], MOVINGDEPTH)
        g.abs_move(point[0]-size, point[1], WRITINGDEPTH)
        g.arc(x=point[0]+size, y=point[1], direction='CCW')
        g.arc(x=point[0]-size, y=point[1], direction='CCW')
        
    def cross(point, size):
        g.abs_move(point[0]-size, point[1]-size, MOVINGDEPTH)
        g.abs_move(point[0]-size, point[1]-size, WRITINGDEPTH)
        g.abs_move(point[0]+size, point[1]+size, WRITINGDEPTH)
        g.abs_move(point[0]+size, point[1]+size, MOVINGDEPTH)
        g.abs_move(point[0]-size, point[1]+size, MOVINGDEPTH)
        g.abs_move(point[0]-size, point[1]+size, WRITINGDEPTH)
        g.abs_move(point[0]+size, point[1]-size, WRITINGDEPTH)
        g.abs_move(point[0]-size, point[1]-size, MOVINGDEPTH)
    
    def dot(point, size):
        g.abs_move(point[0], point[1], MOVINGDEPTH)
        g.abs_move(point[0], point[1], WRITINGDEPTH)
        g.abs_move(point[0], point[1], MOVINGDEPTH)
    for x in list:
        g.abs_move(x[0], x[1], MOVINGDEPTH)
        cross(x, 6)
        g.abs_move(x[0], x[1], MOVINGDEPTH)

def outputFile():
    with open(outfile_path, 'r') as f:
        for line in f:
            print(line)
            # cereal.write(line.encode('utf-8'))
        # cereal.close()

# getGCode(True, [(15,15), (50, 50)])
# outputFile()
