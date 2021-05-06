'''
vid2img.py

Converts video(.mp4 or .avi, etc.) frames into pictures.
'''

import cv2
import os, glob

from configuration import *

i = 0
n_frame = 30

cap = cv2.VideoCapture(vid2img_src)
while(True):
    ret, img = cap.read()
    
    if not ret:
        break
    
    cv2.imwrite(vid2img_dst+"%07d"%i+'.jpg', img)
    i += 1
    print("Saved frame%07d.jpg"%i)
    
    # Use below to get limited pictures per N frame
    # if(int(cap.get(1)) % n_frame == 0):
    #     cv2.imwrite(vid2img_dst+i+'.jpg', img)
    #     print('Saved frame%d.jpg' % i)
    #     i += 1
cap.release()