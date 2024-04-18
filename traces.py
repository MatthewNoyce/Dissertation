from collections import defaultdict

import cv2
import numpy as np

from ultralytics import YOLO,RTDETR

# Load the YOLOv8 model
model = YOLO('c:/Users/matth/Documents/objectdetection/graphsandbestmodels/yolov5l/tracking/weights/best.pt')

# Open the video file
video_path = "c:/Users/matth/Documents/DroneVideoTrackingandDetection/traces.avi"#/annotatedImForWU/tracestest.avi"#/objectdetection/SDSMOT/sds.avi
cap = cv2.VideoCapture(video_path)

# Store the track history
track_history = defaultdict(lambda: [])
out = cv2.VideoWriter('yolov5ltraces.avi',0, 60, (3840, 2160))
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, imgsz=992, conf=0.25, tracker="botsort.yaml")

        # Get the boxes and track IDs
        boxes = results[0].boxes.xywh.cpu()
        #print(results[0].boxes)
        if results[0].boxes.id == None:
            track_ids = []
        else:

            track_ids = results[0].boxes.id.int().cpu().tolist()

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        
        # Plot the tracks
        for box, track_id in zip(boxes, track_ids):
            x, y, w, h = box
            track = track_history[track_id]
            track.append((float(x), float(y)))  # x, y center point
            if len(track) > 1000:  # retain 90 tracks for 1000 frames
                track.pop(0)

            # Draw the tracking lines
            points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
            cv2.polylines(annotated_frame, [points], isClosed=False, color=(0, 0, 230), thickness=10)

        #Need to save the annotated frames to video
        
            out.write(cv2.polylines(annotated_frame, [points], isClosed=False, color=(0, 0, 230), thickness=10))
        
        # Display the annotated frame
        # cv2.namedWindow("YOLOv5 Tracking", cv2.IMREAD_ANYCOLOR)
        # cv2.resizeWindow("YOLOv5 Tracking", 1280,748)
        # # Display the annotated frame
        # cv2.imshow("YOLOv5 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
out.release()
cv2.destroyAllWindows()