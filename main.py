import cv2
import time
import numpy as np
import threading
import tracker
import popper

vid_path = 'test_files/walking.mp4'
cap = cv2.VideoCapture(0)


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

tracker = tracker.Tracker()
printer = popper.Popper()

print_lock = threading.Lock()

def visualize_positions(positions, frame=None):
    if frame is None:
        frame = np.zeros((height, width, 3), dtype=np.uint8)
    for position in positions:
        x, y = position
        cv2.rectangle(frame, (x-5, y-5), (x+5, y+5), (0, 255, 0), 2)
    return frame

def print_thread(positions):
    with print_lock:
        print(positions)
        printer.print(positions)
        time.sleep(60)
        pass

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        positions, annotated_img = tracker.track(frame) 

        scaled_pos = []
        for position in positions:
            x = np.interp(position[0], (0, width), (0, 50))
            y = np.interp(position[1], (0, height), (0, 50))

            scaled_pos.append((x, y))

        cv2.imshow('positions', visualize_positions(positions, frame=frame))

        if not print_lock.locked():
            t = threading.Thread(target=print_thread, args=(scaled_pos,))
            t.start()

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
