import cv2
import numpy as np

wgt = "data/yolov3-320.weights"
cfg = "data/yolov3-320.cfg"
coco = "data/coco.names"

def get_person_coordinates(image_path):
    # Load YOLO model and coco.names (contains class labels)
    net = cv2.dnn.readNet(wgt, cfg)
    with open(coco, "r") as f:
        classes = f.read().strip().split("\n")

    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image.")
        return []

    # Get image dimensions
    height, width = image.shape[:2]

    # Preprocess image
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Get output layer names
    layer_names = net.getLayerNames()
    print(layer_names)
    output_layers = [layer_names[i[0]] - 1 for i in net.getUnconnectedOutLayers()]

    # Run forward pass to get output of the output layers
    outputs = net.forward(output_layers)

    # Initialize lists to store coordinates of people
    person_coordinates = []

    # Process each output
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # Check if object detected is a person and confidence is high enough
            if class_id == 0 and confidence > 0.5:
                # Get coordinates of the bounding box
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Calculate top-left corner coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Append the coordinates to the list
                person_coordinates.append((x, y))

    return person_coordinates
