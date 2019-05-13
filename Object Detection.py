import cv2
import numpy as np

# we point opencv's cascade classifier function to where our classifier (xml file format) is stored
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml.html')

imgpath = '/Users/rajatbhalla/Downloads/President_Barack_Obama.jpg'
image = cv2.imread(imgpath)
img_gray =  cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# our classifier returns the ROI of the detected face as a tuple
# it stores the top left and bottom right coordinates

faces = face_classifier.detectMultiScale(img_gray,1.3,5)


# when no faces detected it returns the empty tuple
if faces is ():
    print("no faces found")

# we iterate through the faces & draw a rectangle
# over each face in faces

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,255),2)
    cv2.imshow('face detection' , image)
    cv2.waitKey(0)

cv2.destroyAllWindows()



