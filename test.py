import cv2
import tracker

cap = cv2.VideoCapture(0)
tracker = tracker.Tracker()

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('positions', frame)

        tracker.track(frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


cap.release()
cv2.destroyAllWindows()
