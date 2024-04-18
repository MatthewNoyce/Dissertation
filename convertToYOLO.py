#converts the given labels into YOLO format labels
#maybe an issue with the y position, it seems to be above the objects instead of over them
import json
with open("C:/Users/matth/Documents/objectdetection/SeaDronesSee_SOT/annotations_json/instances_val_objects_in_water.json", "r") as f:
    g = json.load(f)
    for i in g["annotations"]:
        
        if i["bbox"][2] % 2 == 0:
            x = i["bbox"][0] + i["bbox"][2]/2
        else: 
            x = i["bbox"][0] + (i["bbox"][2] +1)/2
        if i["bbox"][3] % 2 == 0:
            y = i["bbox"][1] + (i["bbox"][3]/2)
        else: 
            y = i["bbox"][1] + (i["bbox"][3] +1)/2
        strin = f"{i['category_id']} {x/3840} {y/2160} {i['bbox'][2]/3840} {i['bbox'][3]/2160}\n"

        file = open(f"C:/Users/matth/Documents/objectdetection/SDSMOT/labels/val/{i['image_id']}.txt", "a")
        
        file.write(strin)
        file.close()