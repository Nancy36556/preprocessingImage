
import cv2
import numpy as np
FILE_NAME ='day2/pic.jpg'
window_name='Scalling Image'
img =cv2.imread(FILE_NAME)
(height,width) = img.shape[:2]
res=cv2.resize(img,(int(width/2),int(height/2)),
       interpolation = cv2.INTER_CUBIC)
cv2.imshow("Source",img)
cv2.imshow(window_name,res)
cv2.waitKey(0)
window_name='Rotation Image'
img = cv2.imread(FILE_NAME)
res=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name,res)
cv2.waitKey(0)
img=cv2.imread(FILE_NAME)
print(img.shape)
cropped_img = img[0:50, 0:50]
cv2.imshow("original", img)
cv2.imshow("Croped", cropped_img)
cv2.waitKey(0)
print("end")