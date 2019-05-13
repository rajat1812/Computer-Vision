
# coding: utf-8

# In[1]:


import cv2
import numpy as np

body_classifier = cv2.CascadeClassifier()
body_classifier.load('/Users/rajatbhalla/Downloads/Haar Cascade Classifiers/haarcascade_fullbody.xml')

cam = cv2.VideoCapture('/Users/rajatbhalla/Downloads/22618951-preview.mp4')

if cam.isOpened():
        ret,frame = cam.read()
        print(ret)
        print(frame)
else :
        ret = False

while ret:
    
    ret,frame = cam.read()

    frame = cv2.resize(frame , None,fx=0.5,fy=0.5,interpolation= cv2.INTER_LINEAR)
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # our classifier returns the ROI of the detected face as a tuple
    # It stores the top left coordinates & the bottom right coordinates
    if body_classifier.empty():
        print("file couldn't load")
    else:
    
        bodies = body_classifier.detectMultiScale(frame_gray,1.3,5)
        print(bodies)

    # Extract bodies from video & bounding box around each body
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("Pedestrians",frame)
        cv2.waitKey(0)
        break


cv2.destroyAllWindows(windowName)
cam.release()

