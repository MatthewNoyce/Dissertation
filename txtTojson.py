import json
import os
#For converting Objectt detection txt files into json files for uploading to the test server

#Need [{"image_id": 123, "category_id":4, "score": 0.5, "bbox":[123,234,345,456]}]
listob = []
txtdir = "C:/Users/matth/Documents/DroneVideoTrackingandDetection/runs/detect/predict/labels"
testjson = "G:/SDSOD/COCO/instances_test.json"


with open(testjson, "r") as tj:
        hw = json.load(tj)
        for image in hw["images"]:
                path = os.path.join(txtdir, (str(image["id"])+".txt"))
                height = image["height"]
                width = image["width"]
                try:
                    f = open(path, "r")
                    for i in f:
                           entry = i.split()
                           xc = float(entry[1])*width
                           yc = float(entry[2])*height
                           w = float(entry[3])*width
                           h = float(entry[4]) *height
                           bbox = [xc-(0.5*w), yc-(0.5*h), w, h]
                           listob += [{"image_id":image["id"], "category_id": int(entry[0]), "score": float(entry[5]), "bbox":bbox}]
                    
                    f.close()
                except FileNotFoundError:
                       next
                


with open("results.json", "w") as fp:
             json.dump(listob, fp)