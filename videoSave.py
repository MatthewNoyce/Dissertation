#saves the video with the annotations on 
import cv2
from ultralytics import YOLO, RTDETR

# Load the model
modelpath = "c:/Users/matth/Documents/objectdetection/graphsandbestmodels/yolov5l/tracking/weights/best.pt"
model = YOLO(modelpath)

# Open the video file
video_path = "C:/Users/matth/Documents/objectdetection/SDSMOT/sds.avi"
cap = cv2.VideoCapture(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output_video.mp4', fps, (width, height))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Write the annotated frame to the output video
        out.write(annotated_frame)

    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture and writer objects and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()