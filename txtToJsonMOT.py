import json
import os
#For converting object tracking txt annotations into MOT json files to upload to the test server
#need a json object [[[]],[[[0.0, 3315.6943359375, 69.73517608642578, 3413.403076171875, 128.14859008789062, 0.9274319410324097], [1.0, -20.059789657592773, 266.204345703125, 119.15104675292969, 389.9878234863281, 0.6445915102958679]]]
#each list should have [object id,bbox_left,bbox_top,bbox_right,bbox_bottom,confidence] for each object in the frame
#txtdir = "C:/Users/matth/Documents/objectdetection/graphsandbestmodels/DETR/tracking/run3/bytetracklabels"
txtdir = "C:/Users/matth/Documents/DroneVideoTrackingandDetection/runs/detect/track/labels"  #"C:/Users/matth/Documents/DroneVideoTrackingandDetection/runs/detect/track/labels"
#txtdir= "C:/Users/matth/Documents/objectdetection/graphsandbestmodels/yolov5l/tracking/labelscstmbytetrack992"
# imagefilesinorder = []
# videoid = []
# frame_id =[]
jsonob = []
nullid=2000

def createList(r1, r2):
    if (r1 == r2):
        return r1
    else:
        res = []
    while(r1 < r2+1 ):
        res.append(r1)
        r1 += 1
    
    return res

#---------------------------------
#DETR NOT WORKING
#WHY IS THIS NOT WORKING
#all that is changed is the image size
#but it is normalised so it shouldnt have an effect at all         
#it worked on imgsz 640
#bounding the edges didnt work 
#The only thing that was altered between the working detr model and this one is the image size
#the image size shouldnt give me any issues because the results are normalised and all bbox size values are in the range they should be 
#All conf values are between 0 and 1
#All tracking ids are integers
#I dont think it is becasue of the size of the track ids
#might be worth checking and resetting the nullid whenever it goes over 10k
#Didnt work 
#---------------------------------

for frame in createList(1, 18253):
    name = f"sds_{frame}.txt"
    
    index = frame-1
    obtowrite = [[]]
    try:
        txt = open(os.path.join(txtdir, name))
        
        for x in txt:
            
            linespl = x.split()
            #l left most pixel
            l=(float(linespl[1])*3840)-((0.5*float(linespl[3]))*3840)
            #t topmost pixel
            t=(float(linespl[2])*2160)-((0.5*float(linespl[4]))*2160) 
            #r rightmost pixel
            r=l+(float(linespl[3])*3840)
            #b bottom most pizel
            b=t+(float(linespl[4])*2160)
            #takes track id from the txt file or gives a "null" if there is no traking with it 
            trackid = int(linespl[6]) if len(linespl) ==7 else nullid
            nullid+=1
            # if nullid % 10000:
            #      nullid=2000
            conf=float(linespl[5]) 
            
           
            obtowrite[0]+=([[trackid,l if l>=0.005 else 0.0,t if t>=0.005 else 0.0,r if r<=3840 else 3840,b if b<=2160 else 2160,conf]])
            
        jsonob+=([obtowrite])
        #print(jsonob)
        txt.close()

    except FileNotFoundError:
               
        jsonob+=([obtowrite])

with open("results_MOT.json", "a") as fp:
            json.dump(jsonob, fp)
