import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

class Pos:
    def __init__(self):
        options = PoseLandmarkerOptions(
            base_options=BaseOptions(model_asset_path='data/pose_landmarker_full.task'),
            running_mode=VisionRunningMode.VIDEO,
            num_poses=100,
            min_pose_detection_confidence=0.3,
            min_pose_presence_confidence=0.3,
            min_tracking_confidence=0.3,
            output_segmentation_masks=False)
        self.detector = PoseLandmarker.create_from_options(options)

    def pos_from_img(self, path):
        image = mp.Image.create_from_file(path)

        detection_result = self.detector.detect(image)

        return detection_result

    def pos_from_vid(self, frame, timestamp):
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

        detection_result = self.detector.detect_for_video(image, timestamp)

        return detection_result


    def draw_landmarks_on_image(self, rgb_image, detection_result):
        pose_landmarks_list = detection_result.pose_landmarks
        annotated_image = np.copy(rgb_image)

        # Loop through the detected poses to visualize.
        for idx in range(len(pose_landmarks_list)):
            pose_landmarks = pose_landmarks_list[idx]

        # Draw the pose landmarks.
        pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        pose_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
        ])
        solutions.drawing_utils.draw_landmarks(
            annotated_image,
            pose_landmarks_proto,
            solutions.pose.POSE_CONNECTIONS,
            solutions.drawing_styles.get_default_pose_landmarks_style())
        return annotated_image
