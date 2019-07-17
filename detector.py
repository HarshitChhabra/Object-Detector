import dlib
import cv2

class ObjectDetector(object):
    def __init__(self,options=None,loadPath=None):

        self.options = options
        if self.options is None:
            self.options = dlib.simple_object_detector_training_options()

        if loadPath is not None:
            self._detector = dlib.simple_object_detector(loadPath)

    def _prepare_annotations(self,annotations):
        annots = []
        for (x,y,xb,yb) in annotations:
            annots.append([dlib.rectangle(left=x,top=y,right=xb,bottom=yb)])
        return annots

    def _prepare_images(self,imagePaths):
        images=[]
        for path in imagePaths:
            print('F:/ObjectDetection/'+path)
            image = cv2.imread(path)
            image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            images.append(image)
        return images

    def fit(self,images,annotations,visualize=False, savePath=None):
        annotations = self._prepare_annotations(annotations)
        images = self._prepare_images(images)
        print('IMAGES',images)
        print('annots',annotations)
        print(self.options)
        self._detector = dlib.train_simple_object_detector(images,annotations,self.options)

        if visualize:
            win = dlib.image_window()
            win.set_image(self._detector)
            dlib.hit_enter_to_continue()
        if savePath is not None:
            self._detector.save(savePath)
        return self

    def predict(self,image):
        boxes = self._detector(image)
        predictions = []
        for box in boxes:
            (x,y,xb,yb)=(box.left(),box.top(),box.right(),box.bottom())
            predictions.append((x,y,xb,yb))
        return predictions

    def detect(self,image,annotations=None):

        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        predictions = self.predict(image)
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        print('hello')
        for (x,y,xb,yb) in predictions:
            cv2.rectangle(image,(x,y),(xb,yb),(0,255,0),2)
            cv2.imshow("Detected",image)
            cv2.waitKey(0)
        win = dlib.image_window()
        win.set_image(self._detector)
        dlib.hit_enter_to_continue()