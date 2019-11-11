import numpy as np
import cv2
import os
import json

class train_data:
    """
    To add new face data.

    """
    def update_iD(self, iD):
        with open(".iD.txt","w") as f:
            f.write("iD = \n"+ str(iD))

    def get_iD(self):
        f = open(".iD.txt","r")
        x = f.readlines()
        iD = int(x[1]) + 1
        f.close()
        self.update_iD(iD)
        return iD
    def rollback(self,iD):
        with open(".iD.txt",'r') as f:
            x = f.readlines()
            iD = int(x[1]) - 1
            self.update_iD(iD)

    def record(self):
        #haarcascade_frontalface_default.xml
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        #training path
        data_path = 'C:/Users/prana/Desktop/practice/python_face_detect/data'

        #Flag
        status = False
        state1 = False
        #getID
        iD = self.get_iD()

        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while 1:
            ret, img = cap.read()
            img = cv2.flip(img,1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5,)

            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                if not state1:
                    cv2.putText(img,'Face Detected', (450,20),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,0),1)
                #need to work here!⛳
                #cv2.putText(img,'Face not Detected', (400,20),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,0),1)

            k = cv2.waitKey(3) & 0xff
            if k == ord('c'):
                try: 
                    if not os.path.exists(os.path.join(data_path + f"./data/{iD}")):
                        os.makedirs(f"./data/{iD}")
                except OSError:
                    print('Error: Creating directory', f"{iD}")
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)   
                    state1 = cv2.imwrite(os.path.join(data_path + f"{iD}" ,f'ID{iD}_faces.jpg'), img)
                    roi_color = img[y:y + h, x:x + w]
                    status = cv2.imwrite(os.path.join(data_path + f"{iD}" ,f'ID{iD}_faces_roi.jpg'), roi_color)
                break
            cv2.putText(img,'Press " c " to capture ', (10,20),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,0),1)
            cv2.imshow('img',img)
        cap.release()
        cv2.destroyAllWindows()

        if status == False:
            #self.rollback(iD)
            pass
        print("Data is stored.", status, state1)