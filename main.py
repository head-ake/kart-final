import cv2
import numpy as np
import threading
import tracker
import printer

vid_path = 'test_files/walking.mp4'
cap = cv2.VideoCapture(vid_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

tracker = tracker.Tracker()
printer = printer.Printer()

print_lock = threading.Lock()

def visualize_positions(positions):
    black_frame = np.zeros((height, width, 3), dtype=np.uint8)
    for position in positions:
        x, y = position
        cv2.rectangle(black_frame, (x-5, y-5), (x+5, y+5), (0, 255, 0), 2)
    return black_frame

def print_thread(positions):
    with print_lock:
        printer.print(positions)
        pass

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        positions, annotated_img = tracker.track(frame) 

        cv2.imshow('positions', visualize_positions(positions))

        if not print_lock.locked():
            t = threading.Thread(target=print_thread, args=(positions,))
            t.start()

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
