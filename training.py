from ultralytics import RTDETR, YOLO

#possibly worth reducing patience down to 20 for detr and yolo5l due to how long they take to train and the last 50 or so epochs give mostly the same value anyway
def main():
    trackingyaml = "C:/Users/matth/Documents/objectdetection/graphsandbestmodels/yolov5m/tracking/seadronessee.yaml"
    obdetyaml = "C:/Users/matth/Documents/objectdetection/graphsandbestmodels/sdsOD.yaml"
    #Training scripts for the yolo and detr based architectures
    def detr(trackingyaml):
        #using resume=True since takes a long time to run and pc si unusable while it is running
        #might be worth reducing the number of dataloader workers to reduce the amount of vram usage(or upgrade gpu lol)
        #going to take so much longer for tracking task since it is like 9x the size of this dataset
        #seem to be having issues with using batchseze=4, might have to redo training for tracking overnight with higher batch size
        #also might just need to train for more than 100 epochs. will see how the curves look when the first test is done. 
        #lots of issues with batch size 4 so increase to 8. will still take a lot of vram so going to have to train overnight 
        #ends up about 35 minutes with screen off so just keep training overnight and see how it does
        model = RTDETR("rtdetr-resnet50.yaml") #rtdetr-resnet50.yaml C:/Users/matth/Documents/DroneVideoTrackingandDetection/runs/detect/train/weights/last.pt
        model.train(data=trackingyaml, epochs=100, imgsz=850, batch=4, patience=15) #, resume=True
        
    def yolo5m(obdetyaml):
        #could be worth trying a larger image size to see if it can pick up smaller objects easier
        model = YOLO("yolov5m.yaml")
        model.train(data=obdetyaml, epochs=300, imgsz=850, batch=8) 
    def yolo5l(trackingyaml): #10gb vram 2 hours per iteration on the mot dataset with batch=16
        resumetraining = "C:/Users/matth/Documents/DroneVideoTrackingandDetection/runs/detect/train/weights/last.pt" #resumetraining
        model = YOLO("yolov5l.yaml") #takes a lot less time with batch=8 workers=4. might be worth increasing workers back to 8 tho 
        model.train(data=trackingyaml, epochs=300, imgsz=750, workers=4, batch=8) #, resume=True
    def yolo5s(trackingyaml): #4gb vram with imgsz=640, maybe increase image size for training 
        resumetraining = "C:/Users/matth/Documents/DroneVideoTrackingandDetection/runs/detect/train/weights/last.pt"
        fromscratch = "yolov5s.yaml"
        model = YOLO(fromscratch)
        model.train(data=trackingyaml, epochs=300, imgsz=850) #, resume=True
    def rtdetr(trackingyaml):
        model = RTDETR("rtdetr-l.yaml") #rtdetr-l.yaml C:/Users/matth/Documents/DroneVideoTrackingandDetection/runs/detect/train/weights/last.pt
        model.train(data=trackingyaml, epochs=100, imgsz=850, batch=4, patience=15, resume=True)

    #is it worth doing v8 as well? could take out faster rcnn from the paper and try v8 instead as they are both still cnns.

    rtdetr(obdetyaml)
    #detr(trackingyaml)
    #yolo5s(obdetyaml)
    #yolo5m(obdetyaml)
    #yolo5l(obdetyaml)

    

if __name__ == "__main__":
    main()