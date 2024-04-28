import json
import os
#Not needed anymore, this was for tracking only swimmers which was an expired format for the test server

txtdir = "C:/Users/matth/Documents/DroneVideoTrackingandDetection/runs/detect/track/labels"
imagefilesinorder = []
videoid = []
frame_id =[]

def createList(r1, r2):
    if (r1 == r2):
        return r1
    else:
        res = []
    while(r1 < r2+1 ):
        res.append(r1)
        r1 += 1
    return res

with open("C:/Users/matth/Documents/objectdetection/SeaDronesSee_SOT/annotations_json/instances_test_swimmer.json", "r") as f:
    file = json.load(f)
    for i in file["images"]:
        imagefilesinorder.append(i["id"])
        videoid.append(i["video_id"]) 
        frame_id.append(i["frame_index"])
        #print(videoid)
for frame in createList(0, 18259):
    name = f"myvideo_{frame}.txt"
    #vidframe = int(name)
    index = frame-1
    try:
        txt = open(os.path.join(txtdir, name))
        for x in txt:
            linespl = x.split()
            #print(linespl)  
            x=(float(linespl[1])-(0.5*float(linespl[3])))*3840
            y=(float(linespl[2])-(0.5*float(linespl[4])))*2160
            w=float(linespl[3])*3840
            h=float(linespl[4])*2160
            trackid = int(linespl[5]) if len(linespl) ==6 else 0
            obtowrite = f"{frame_id[index]},{trackid},{x},{y},{w},{h}\n"
            #print(obtowrite)
            #print(videoid[index])
            file = open(f"swimmer/{videoid[index]}.txt", "a")
            file.write(obtowrite)
            file.close()
        
        
        txt.close()
    except FileNotFoundError:
        next
    # txt = open(os.path.join(txtdir, (str(id)+".txt")))
    # for x in txt:
    #     linespl = x.split(" ")
    #     print(linespl)    


# print(videoid)
# print(imagefilesinorder)
# print(frame_id)