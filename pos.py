from collections import defaultdict

import cv2
import numpy as np

from ultralytics import YOLO

model = YOLO('data/yolov8n.pt')

video_path = 'test_files/walking.mp4'
cap = cv2.VideoCapture(video_path)

track_history = defaultdict(lambda: [])

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        results = model.track(frame, persist=True)

        annotated_frame = results[0].plot()

        cv2.imshow("tracking", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

