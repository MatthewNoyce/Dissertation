import os
import cv2
import json 
#To add the test images into a video to display the tracking capabilities
#produces a ffull video compiling all test videos into one 

imagefilesinorder = []
vidfiles = ["DJI_0001.mov", "DJI_0051.MP4", "DJI_0065.MP4", "DJI_0001_d3.mov", "DJI_0039.MP4", "DJI_0003.mov", "DJI_0064.MP4", "DJI_0069.MP4", "DJI_0011_d3.mov", "DJI_0057.MP4", "DJI_0032.MP4",  "DJI_0001.MOV", "DJI_0010_d3.mov","DJI_0063.MP4", "DJI_0059.MP4", "DJI_0006_d3.mov",  "DJI_0055.MP4", "DJI_0041.MP4","DJI_0038.MP4"]
print(len(vidfiles))
with open("C:/Users/matth/Documents/objectdetection/SeaDronesSee_SOT/annotations_json/instances_test_objects_in_water.json", "r") as f:
    file = json.load(f)
    print(len(file["images"]))
    for vid in vidfiles:
        for i in file["images"]:
            if i["source"]["video"] == vid:

                imagefilesinorder.append(i["id"])
            else:
                next
print(imagefilesinorder)    
print(len(imagefilesinorder))
def generate_video():
    counter=0
    image_folder = 'c:/Users/matth/Documents/objectdetection/SDSMOT/images/test'
    video_name = 'sds.avi'
    os.chdir("c:/Users/matth/Documents/objectdetection/SDSMOT/")



    frame = cv2.imread(os.path.join(image_folder, f"{imagefilesinorder[0]}.jpg"))   
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 30, (width, height))

    for image in imagefilesinorder:        
        video.write(cv2.imread(os.path.join(image_folder, f"{image}.jpg")))
        counter+=1
        print(counter)
    cv2.destroyAllWindows()
    video.release()
generate_video()
