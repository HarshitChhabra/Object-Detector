# Object-Detector
This is an Image Processing and Machine Learning based project which can be used to train and create a detector which can be used to detect any object (Faces, Pedestrian, etc). It uses SVM provided by Dlib.

**Note:** Make sure you have [dlib](http://dlib.net/) installed.

## Instructions:
1. First run **gather_annotations.py** to create training dataset. 

    Required Arguements:
    
      "-d" ("--dataset") = path to images dataset.
      
      "-a" ("--annotations") = path to save annotations.
      
      "-i" ("--images") = path to save images.
      
 2. Next, run **train.py** to create the svm based detector. 
 
    Required Arguements:
        
      "-a" ("--annotations") = path to saved annotations.
      
      "-i" ("--images") = path to saved image paths.
      
      "-d" ("--detector") = path to save the trained detector.
      
Now, the detector is ready and .svm file can be found in the path specified.

To test, run **test.py** with following arguements:

    "-d" ("--detector") = path to trained detector to load.
    
    "-i" ("--image") = path to an image for object detection.
