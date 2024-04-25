import logging
from ultralytics import YOLO

class Tracker:
    def __init__(self):
        self.model = YOLO('data/yolov8n.pt')
        logging.getLogger('ultralytics').setLevel(logging.WARNING)
        return

    def track(self, img):
        results = self.model.track(img, persist=True)
        boxes = results[0].boxes.xywh.cpu()
        points = []
        for box in boxes:
            x, y, _, _ = box
            points.append((int(x), int(y)))

        annotated_img = results[0].plot()
        return points, annotated_img

