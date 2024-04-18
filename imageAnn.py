import cv2
from ultralytics import RTDETR, YOLO
import os
#Program to produce annotated results and examples for the write up
def imagebboxann():
    frame = cv2.imread("g:/SDSOD/YoloFormat/images/train/563.png")
    #labels for image 563
    #2 0.953721 0.0121145 0.00421554 0.00715859
    #2 0.945015 0.0174835 0.00293255 0.00743392
    #imsize = 5456x3632
    l1x = int(0.953721*5456)
    l1y = int(0.0121145*3632)
    l1x2 = int(l1x + (0.00421554*5456))
    l1y2 = int(l1y + (0.00715859*3632))
    l2x = int(0.945015*5456)
    l2y = int(0.0174835*3632)
    l2x2 = int(l2x + (0.00293255*5456))
    l2y2 = int(l2y + (0.00743392*3632))
    #l1sp = (l1x,l1y)
    #l1ep=(l1x2,l1y2)
    colour = (0, 255, 0)
    thickness = 6
    image = cv2.rectangle(frame, (l1x,l1y), (l1x2,l1y2), colour, thickness) 
    image = cv2.rectangle(frame, (l2x,l2y), (l2x2,l2y2), colour, thickness) 
    resized_image = cv2.resize(image, (640, 426)) 
    # cv2.imwrite("563resized.png", resized_image)
    # cv2.namedWindow("image", cv2.IMREAD_ANYCOLOR)
    # cv2.resizeWindow("image", 1280,748)
    # cv2.imshow("image", image)
    # cv2.waitKey(0)
def odshow():
    model=RTDETR("C:/Users/matth/Documents/objectdetection/graphsandbestmodels/DETR/tracking/rt-detrl/weights/best.pt")
    frames= ["C:/Users/matth/Documents/objectdetection/SDSMOT/images/test/41763.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/test/25517.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/test/15324.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/test/14692.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/test/12182.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/test/11175.jpg"]
    model.predict(frames, save=True, imgsz=640, conf=0.25) #, conf=0.5
    
def motshow():
    model=YOLO("C:/Users/matth/Documents/objectdetection/graphsandbestmodels/yolov5m/tracking/objects_in_water/train11/weights/best.pt")
    video = "example.avi"
    model.track(video, save=True, persist=True, imgsz=640)

def generate_video():
    counter=0
    image_folder = 'c:/Users/matth/Documents/objectdetection/SDSMOT/images/test'
    #frames = ["C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2061.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2062.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2063.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2064.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2065.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2066.jpg","C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2067.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2068.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2069.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2070.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2071.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2072.jpg","C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2073.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2074.jpg", "C:/Users/matth/Documents/objectdetection/SDSMOT/images/train/2075.jpg"]
    frames = []
    video_name = 'traces.avi'
    for i in range(53470, 53800):
        # num = str(i)
        # num = "000"+num
        # num = num[-3:]
        # #print(num)
        # imgname = f"2{num}"
        frames.append(os.path.join(image_folder, f"{i}.jpg")) 


    frame = cv2.imread(frames[0])   
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 30, (width, height))

    for image in frames:        
        video.write(cv2.imread(image))
        counter+=1
        print(counter)
    cv2.destroyAllWindows()
    video.release()

def getframes():
    capture = cv2.VideoCapture(r'C:\Users\matth\Documents\DroneVideoTrackingandDetection\yolov5ltraces.avi')
    frameNr = 0
    while (True):
        success, frame = capture.read()
        if success:
            print(frameNr)
            if not cv2.imwrite(f"C:/Users/matth/Documents/DroneVideoTrackingandDetection/traces/frame_{frameNr}.jpg", frame):
                raise Exception("Could not write image")
        else:
            print("bad")
            break
        frameNr = frameNr+1
    capture.release()
#odshow()
#motshow()
#generate_video()
getframes()