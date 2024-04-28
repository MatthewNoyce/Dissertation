#Runns detection using a trained model and saves results as text files

from ultralytics import RTDETR, YOLO
import json
# import os
def main():
    
    counter=0
    model = YOLO("C:/Users/matth/Documents/objectdetection/graphsandbestmodels/yolov5m/detection/train1/weights/best.pt")
    #model.predict(source="G:/seedronessea/YoloFormat/images/test/130.png", save=True, imgsz=320, conf=0.5) #, save_json=True show=True, 

    # Define path to directory containing images and videos for inference
    source = 'G:/SDSOD/YoloFormat/images/test/*.png'
    # Run inference on the source
    
    results = model.predict(source=source, save_txt=True, save_conf=True, stream=True, conf=0.5, iou=0.99, imgsz=992) 
    # generator of Results objects
    for result in results:
        counter+=1
        print(counter)
        
    

if __name__ == "__main__":
    main()