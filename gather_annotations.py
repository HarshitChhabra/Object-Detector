import numpy as np
import argparse
import cv2
from BoxSelector import BoxSelector
from imutils.paths import list_images

ap = argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,help="path to images dataset...")
ap.add_argument("-a","--annotations",required=True,help="path to save annotations...")
ap.add_argument("-i","--images",required=True,help="path to save images")
args = vars(ap.parse_args())

annotations = []
imagePaths = []
for image_path in list_images(args["dataset"]):

    image = cv2.imread(image_path)
    boxSelector = BoxSelector(image,"Image")
    cv2.imshow("Image",image)
    cv2.waitKey(0)

    pt1,pt2 = boxSelector.getStartAndEnd
    (x,y,xb,yb)=(pt1[0],pt1[1],pt2[0],pt2[1])
    annotations.append([int(x),int(y),int(xb),int(yb)])
    imagePaths.append(image_path)

annotations = np.array(annotations)
imagePaths = np.array(imagePaths,dtype="unicode")
np.save(args["annotations"],annotations)
np.save(args["images"],imagePaths)