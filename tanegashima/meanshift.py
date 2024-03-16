import cv2
import numpy as np

print("nkdklgfasklfjasdklj")
img=cv2.imread("./corn/1.jpg")
src=cv2.pyrMeanShiftFiltering(img, )
cv2.imwrite("./mean/a.jpg",src)
print("hello")