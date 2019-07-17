import numpy as np
import cv2

class BoxSelector:
    def __init__(self,image,window_name,color = (0,0,255)):
        self.image = image
        self.window_name = window_name
        self.color = color

        self.original = image.copy()

        self.track = False
        self.start = None
        self.end = None

        cv2.namedWindow(window_name)
        cv2.setMouseCallback(self.window_name, self.mouseCallBack)

    def mouseCallBack(self, event, x, y, flags, params):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.start = (x,y)
            self.track = True

        elif self.track == True and (event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_MOUSEMOVE):
            self.end = (x,y)

            if self.start != self.end:
                self.image= self.original.copy()
                cv2.rectangle(self.image,self.start,self.end,self.color,1)

                if event == cv2.EVENT_LBUTTONUP:
                    self.track = False
            else:
                self.image = self.original.copy()
                self.track = False
                self.start = None
                self.end = None
            cv2.imshow(self.window_name,self.image)

    @property
    def getStartAndEnd(self):
        if self.start and self.end:

            pts = np.array([self.start,self.end])
            tempSum = np.sum(pts,axis=1)
            (x,y) = pts[np.argmin(tempSum)] #Setting starting position as minimum (lower x,y coordinates) of the two coordinates and ending as the other
            (xb,yb) = pts[np.argmax(tempSum)]
            return [(x,y),(xb,yb)]
        else:
            return []
