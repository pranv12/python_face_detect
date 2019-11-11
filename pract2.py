import cv2
import os

 #haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        #training path
data_path = 'C:/Users/prana/Desktop/practice/python_face_detect/data'
cap = cv2.VideoCapture(0)
#Flag
status = False
f = open(".iD.txt","r")
x = f.readlines()
iD = int(x[1]) + 1
f.close()
f = open(".iD.txt","w")
f.write("iD = \n"+ str(iD))
f.close()
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5,)
    
    for (x,y,w,h) in faces:
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imwrite(os.path.join(data_path ,f'ID{iD}_faces.jpg'), img)
        roi_color = img[y:y + h, x:x + w]
        status = cv2.imwrite(os.path.join(data_path ,f'ID{iD}_faces_roi.jpg'), roi_color)
        print("Data is stored.", status)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()