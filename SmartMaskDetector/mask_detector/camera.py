import numpy as np
import cv2
import joblib
import os
from django.conf import settings

svm=joblib.load(os.path.join(settings.BASE_DIR,'mask_detector/FaceDetectorModel1.pkl'))
haar_data=cv2.CascadeClassifier(os.path.join(settings.BASE_DIR,'mask_detector/haar_face_detector.xml'))
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

class WebCam(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        flag, img=self.video.read()
        names={0:'Mask',1:'No Mask'}
        if flag:
            faces=haar_data.detectMultiScale(img)
            for x,y,w,h in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 4)
                face=img[y:y+h, x:x+w, :]
                face=cv2.resize(face, (100,100))
                face=face.reshape(1, -1)
                pred=svm.predict(face)
                n=names[int(pred)]
                #print(n)
                if n=='Mask':
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 4)
                    cv2.rectangle(img, (x, y-50), (x+150, y-5), (0,255,0), -1)
                    cv2.putText(img,n,(x+10,y-10), font, 1.2, (255, 255, 255), 2)
                else:
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 4)
                    cv2.rectangle(img, (x, y-50), (x+190, y-5), (0,0,255), -1)
                    cv2.putText(img,n,(x+10,y-10), font, 1.2, (255, 255, 255), 2)
                    
            ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes() 