from imageai.Detection.Custom import CustomVideoObjectDetection
from imageai.Detection import VideoObjectDetection
import os
import cv2
import datetime

var1 = 0
var2 = 0
count = 1
path_to_videos = '<Enter Path>'  # Path of folder where your videos are placed

path_for_frames = '<Enter Path>' # Path where you want to store the resultant detected frames

## For Person
def forFrame1(frame_number, output_array, output_count, detected_frame):

    global var1
    global count

    if len(output_count) > 0:
        var1 += 1
    
    if var1 == 4:
        #var1 = 0
        cv2.imwrite(path_for_frames + '/' + "frame%d.jpg" % count, detected_frame)
        count += 1

## For Gun
def forFrame2(frame_number, output_array, output_count, detected_frame):

    global var2
    global count

    if len(output_count) > 0:
        var2 += 1
    
    if var2 == 4:
        #var2 = 0
        cv2.imwrite(path_for_frames + '/' + "frame%d.jpg" % count, detected_frame)
        count += 1



## Person Detector
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel(detection_speed = "fastest")
custom_objects = detector.CustomObjects(person=True)

## Gun Detector
video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath("guns/models/detection_model-ex-007--loss-0007.753.h5")
video_detector.setJsonPath("guns/json/detection_config.json")
video_detector.loadModel()


for r, d, f in os.walk(path_to_videos):
        for file in f:
                hour = int(datetime.datetime.fromtimestamp(os.stat(str(path_to_videos) + '/' + str(file)).st_birthtime).hour)
                print(hour)
                if hour >= 20 or hour <= 6:
                        video_path = detector.detectCustomObjectsFromVideo(custom_objects=custom_objects, 
                                                                        input_file_path=str(path_to_videos) + '/' + str(file),
                                                                        save_detected_video=False,
                                                                        per_frame_function=forFrame1,
                                                                        minimum_percentage_probability=20,
                                                                        log_progress=True,
                                                                        return_detected_frame=True)
                        var1 = 0
                else:
                        video_detector.detectObjectsFromVideo(input_file_path=str(path_to_videos) + '/' + str(file),
                                                                save_detected_video=False,
                                                                per_frame_function=forFrame2,
                                                                frames_per_second=50,
                                                                minimum_percentage_probability=50,
                                                                log_progress=True,
                                                                return_detected_frame=True)
                        var2 = 0