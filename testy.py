#For testing my submission against the sample submission. 


import json
counter=0
counter1=0
# with open("C:/Users/matth/Documents/objectdetection/SeaDronesSee_SOT/MOT_example_submission.json", "r") as f:
#     file=json.load(f)
#     #print(file[13000])
#     print(len(file))
#     for r in file:
#         for x in r:
#             for i in x:
#                 counter1+=1
   # print(file[100][0][0])
    # for r in file:
    #     for x in r:
    #         for i in x:
    #             if i[1]>3840 or i[3]>3840:
    #                 print(i)
#     print(file[100])
# #     #for i in file:
        
#         #print(i)
# #print(counter)
# with open("C:/Users/matth/Documents/objectdetection/SeaDronesSee_SOT/annotations_json/instances_test_objects_in_water.json", "r") as fp:
#     vid=""
#     f=json.load(fp)
#     for image in f["images"]:
#         counter+=1
#         if image["source"]["video"]!= vid:
            
#             vid = str(image["source"]["video"])
#             print(vid)
#     print(counter)
    


maxlen = 0
with open("results_MOT.json", "r") as fp: #
    file=json.load(fp)
    temp=0
    print(len(file))
    # for r in file:
    #     for x in r:
    #         # if len(x) > maxlen:
    # #             maxlen = len(x)
    # # print(maxlen)
    #         print(x)
    #         for i in x:
                #if i[3] - i[1] <= 0 or i[4]-i[2] <=0:
                    #print(i)
                # if i[5] >=1 or i[5]<=0:
                #     print(i)
               # next
                # temp = i[0]
                #print(i[0])
            #     if type(i[0]) != int :
            #         print(i)
            # print(len(file))
    # print(counter1)
    # print(counter)
######################################################################
#Checked length of all entries in results
#checked that conf is between 0 and 1
#checked left is less than right and top is less than bottom
#checked length of files
#checked index is always positive
#checked that every type is float
#checked that id is an int
#have 19 vid files and 18253 frames
#i have more detections than the sample but it shouldnt matter
#[100][0][0] gives one detection from a frame for each
#[100][0] gives all detections within a list [[],[],[]]
#[100] gives the same as [100][0] except within two lists
#changing the spacing between the commas doesnt work 
#each frame has double square brackets around it and each object has square brackets
#everything is inside one list
#checked that all coordinates are inside the image boundaries
#completely empty submission works fine, i.e filenotfound for every item in list
#tested a submission of exactly one object detected with no other entries
#tested completely empty submission with exactly one object detected which works
    #must be something to do with multiple detections per frame
#works with one detection per frame that has an object detected in it
#doesnt work with at most 2 detections per frame so something is wrong with the format of multiple detections per frame
#tried += instead of .append didnt work 
#something is not working with multiple detections per frame
#is it to do with having the same id on multiple objects in the same frame YES
#changed nullid from constantly 0 to an incremental counter so that there wasnt the same id in the same frame
    