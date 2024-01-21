import cv2
import numpy as np
import time


def img_estim(img, thrshld):
    is_light = np.mean(img) > thrshld
    print(np.mean(img))
    return 'light' if is_light else 'dark'


cap=cv2.VideoCapture('http://172.16.83.248:8080/video')

success, img = cap.read()
print(img_estim(img, 100))
 
