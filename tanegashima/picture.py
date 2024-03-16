#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
#import picamera
import numpy as np
import random
import sys
import cv2
import time


def red_detect(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_min = np.array([0, 50, 0])
    hsv_max = np.array([0, 250, 0])
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

    hsv_min = np.array([0, 170, 150])
    hsv_max = np.array([20, 255, 255])  # (90,255,255)でうまくいったけどmaxが255じゃないっぽい
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

    return mask1 + mask2


def main():

    for j in range(1, 26, 1):
        image1 = cv2.imread('./corn/'+str(j)+'.jpg')
        #image1 = cv2.imread('./test1.jpeg')
        #image = cv2.GaussianBlur(image1,(5,5),3)#delete white noise
        image = cv2.GaussianBlur(image1, (3, 3), 1)  # delete white noise
        mono_src = red_detect(image)
        cv2.imshow('RED_DETECT', mono_src)
        color_src01 = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)
        color_src02 = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)
        label = cv2.connectedComponentsWithStats(
            mono_src)  # make array to get imformation
        if label:
            n = label[0] - 1
            data = np.delete(label[2], 0, 0)
            center = np.delete(label[3], 0, 0)
            #print(label[3])dddddddddddddddddd
        for i in range(n):
            x0 = data[i][0]
            y0 = data[i][1]
            x1 = data[i][0] + data[i][2]
            y1 = data[i][1] + data[i][3]
            cv2.rectangle(color_src01, (x0, y0), (x1, y1), (0, 0, 255))
            cv2.rectangle(color_src02, (x0, y0), (x1, y1), (0, 0, 255))
            cv2.putText(color_src01, "ID: " + str(i + 1), (x1 - 20,
                                                           y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
            cv2.putText(color_src01, "S: " + str(
                data[i][4]), (x1 - 20, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
            cv2.putText(color_src02, "X: " + str(
                int(center[i][0])), (x1 - 30, y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
            cv2.putText(color_src02, "Y: " + str(
                int(center[i][1])), (x1 - 30, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))

        cv2.imwrite('./b/'+str(j)+'.jpg', color_src02)

    print("finish")


if __name__ == '__main__':
    main()
