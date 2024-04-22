import time
import pos
import cv2
import numpy as np


img_path = "data/test_imgs/office_a.jpeg"

coordinates = pos.get_person_coordinates(img_path)
print("Person coordinates (x, y) in the room:", coordinates)

'''
# Display the image
cv2.imshow("Image", img)

# Wait for a key press infinitely until the user exits
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
vid_path = "data/test_imgs/walking_a.mp4"

cap = cv2.VideoCapture(vid_path)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    results = positioner.pos_from_vid(frame, int(time.time() * 1000))

    if len(results.pose_landmarks) > 0:
        marked_frame = positioner.draw_landmarks_on_image(frame, results)
        cv2.imshow('vid', marked_frame)
    else:
        cv2.imshow('vid', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

'''



