
import matplotlib.pyplot as plt
import cv2
import numpy as np
color_image=cv2.imread('day7/girle.jpg')
color_image1=cv2.imread('day7/salet.jpg')
gray_img= cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
gray_img1= cv2.cvtColor(color_image1, cv2.COLOR_BGR2GRAY)
sliding_window_size_x=3
sliding_window_size_y=3
mean_filter_kernal=np.ones((sliding_window_size_x,sliding_window_size_y),np.float32)/(sliding_window_size_x*sliding_window_size_y)
filter_img = cv2.filter2D(gray_img,-1,mean_filter_kernal)
filter_mid = cv2.medianBlur(gray_img,3)
filter_img1 = cv2.filter2D(gray_img1,-1,mean_filter_kernal)
filter_mid1 = cv2.medianBlur(gray_img1,3)
plt.subplot(231),plt.imshow(gray_img,cmap=plt.cm.gray), plt.title("1")
plt.subplot(232),plt.imshow(filter_img ,cmap=plt.cm.gray), plt.title("2")
plt.subplot(234),plt.imshow(gray_img1 ,cmap=plt.cm.gray), plt.title("3")
plt.subplot(233),plt.imshow(filter_mid,cmap=plt.cm.gray), plt.title("4")
plt.subplot(235),plt.imshow(filter_img1,cmap=plt.cm.gray), plt.title("5")
plt.subplot(236),plt.imshow(filter_mid1,cmap=plt.cm.gray), plt.title("6")
plt.xticks([]), plt.yticks([])
plt.show()





