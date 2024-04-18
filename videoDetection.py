import cv2
from ultralytics import YOLO, RTDETR

# Load the YOLOv5 model
#model = YOLO('C:/Users/matth/Documents/dronevideotrackinganddetection/runs/detect/train/weights/best.pt')
model = RTDETR('C:/Users/matth/Documents/objectdetection/graphsandbestmodels/DETR/tracking/run3/weights/best.pt')
# Open the video file
video_path = "c:/Users/matth/Documents/objectdetection/SDSMOT/sds.avi"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, imgsz=1280, tracker="C:/Users/matth/Documents/objectdetection/ultralytics-main/ultralytics-main/ultralytics/cfg/trackers/custom.yaml") #imgsz=1280,

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        cv2.namedWindow("YOLOv5 Tracking", cv2.IMREAD_ANYCOLOR)
        cv2.resizeWindow("YOLOv5 Tracking", 1280,748)
        # Display the annotated frame
        cv2.imshow("YOLOv5 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()