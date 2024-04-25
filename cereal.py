import serial # pip install serial
import time

printer_port = 'printer serial port'
baud = 115200
cereal = serial.Serial(printer_port, baud, timeout=1)
home = "G28"

def send_gcode(gcode):
    cereal.write(gcode.encode('utf-8'))
    # possibly add some delay

try:
    while True:
        # pull new or accept new data
        gcode_command = "some gcode based on new data"
        send_gcode(gcode_command)

        send_gcode(home)

        time.sleep(5) # delay or something until new data or whatever

except KeyboardInterrupt:
    cereal.close()