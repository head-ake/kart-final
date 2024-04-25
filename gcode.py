from mecode import G
def getGCode(toFile: bool, list):
    WRITINGDEPTH = 0
    MOVINGDEPTH = 15
    g = G(outfile=r'C:/Users/edmun/Desktop/ArtFinal/file.gcode')

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

    for x in list:
        g.abs_move(x[0], x[1], MOVINGDEPTH)
        cross(x, 5)
        g.abs_move(x[0], x[1], MOVINGDEPTH)
        
getGCode(True, [(15,15), (50, 50)])