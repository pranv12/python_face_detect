import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Write some Text

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 0.5
fontColor              = (255,255,255)
lineType               = 2

cv2.putText(img,'Press " y " to capture ', (10,500),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)

#Display the image
cv2.imshow("img",img)

#Save image
cv2.imwrite("out.jpg", img)

cv2.waitKey(0)