The files that are required to run this program are tracker.py, popper.py, and main.py
System overview is opencv loads YOLO object classification model (different from media pipe), the model processes frames, and that data is converted to gcode and passed through a serial connection to the printer.


to get the model run
`wget https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt`
and place the downloaded file in the data directory

`pip install ultralytics` 

if you want to write test code for the printer put it in the `if __init__ = '__main__'` block and it'll run with `python3 printer.py`
