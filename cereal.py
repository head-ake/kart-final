import serial # pip install serial
import time

printer_port = 'COM3'
baud = 115200
cereal = serial.Serial(printer_port, baud, timeout=1)
home = "G28"

test_cmd = "G1 X100 Y100 Z20 F3000\n"
center_cmd = "G1 X110 Y110 Z20 F3000\n"
square_test = [
    "G1 X10 Y10\n",    # Bottom-left corner
    "G1 X10 Y190\n",   # Top-left corner
    "G1 X190 Y190\n",  # Top-right corner
    "G1 X190 Y10\n",   # Bottom-right corner
    "G1 X10 Y10\n"     # Return to starting position
]

def send_gcode(gcode):
    cereal.write(gcode.encode('utf-8'))
    # possibly add some delay

send_gcode(center_cmd)
time.sleep(1)
for test in square_test:
    send_gcode(test)
    time.sleep(1)

time.sleep(1)
send_gcode(center_cmd)
cereal.close()

# try:
#     while True:
#         # pull new or accept new data
#         gcode_command = "some gcode based on new data"
#         send_gcode(gcode_command)

#         send_gcode(home)

#         time.sleep(5) # delay or something until new data or whatever

# except KeyboardInterrupt:
#     cereal.close()