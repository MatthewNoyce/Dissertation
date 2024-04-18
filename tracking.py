from ultralytics import YOLO, RTDETR
import json
#Needs to be completed, need it to produce an output in the format to upload to the test server
def main():
    counter = 0
    model =     RTDETR("c:/Users/matth/Documents/objectdetection/graphsandbestmodels/DETR/tracking/rt-detrl/weights/best.pt")
    botsort = "botsort.yaml"
    bytetrack = "bytetrack.yaml"
    custombotsort = "C:/Users/matth/Documents/objectdetection/graphsandbestmodels/custombotsort.yaml"
    custombytetrack = "C:/Users/matth/Documents/objectdetection/graphsandbestmodels/custombytetrack.yaml"
    results = model.track(source="c:/Users/matth/Documents/objectdetection/SDSMOT/sds.avi", persist=True, imgsz=850, show=False, save=False, stream=True, save_txt=True, save_conf=True, tracker=custombytetrack, conf=0.4)
    
    
    for result in results:
        counter+=1
        print(counter)
    
  
if __name__ == "__main__":
    main()