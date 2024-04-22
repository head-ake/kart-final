import cv2
import numpy as np
import tracker

vid_path = 'test_files/walking.mp4'
cap = cv2.VideoCapture(vid_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

black_frame = np.zeros((height, width, 3), dtype=np.uint8)

tracker = tracker.Tracker()

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        points, annotated_img = tracker.track(frame) 

        black_frame_copy = black_frame.copy()
        for point in points:
            x, y = point
            cv2.rectangle(black_frame_copy, (x-5, y-5), (x+5, y+5), (0, 255, 0), 2)

        cv2.imshow('rect', black_frame_copy)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
