import numpy as np
import cv2
import os

class check:
    """
    To compare input image with database.

    """
    
    def capture_new(self):
        #haarcascade_frontalface_default.xml
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        #Testing path
        results_path = 'C:/Users/prana/Desktop/practice/python_face_detect/results'

        #capture video
        cap = cv2.VideoCapture(0)


        while 1:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5,)

            for (x,y,w,h), i in zip(faces,range(10)):
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.imwrite(os.path.join(results_path ,f'ID{i}_faces.jpg'), img)
                roi_color = img[y:y + h, x:x + w]
                status = cv2.imwrite(os.path.join(results_path ,f'ID{i}_faces_roi.jpg'), roi_color)
                
            if status == True:
                break

        cv2.imwrite('ROI',roi_color)

        cap.release()
        cv2.destroyAllWindows()



    def checker(self):
        pass