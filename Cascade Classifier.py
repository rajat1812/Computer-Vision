
import cv2
import numpy as np

# we point opencv's Cascade classifier function to
# where our classifier is stored (xml file format)

face_classifier = cv2.CascadeClassifier()
face_classifier.load('/Users/rajatbhalla/Downloads/haarcascade_eye.xml')

image = cv2.imread("/Users/rajatbhalla/Downloads/hPresident_Barack_Obama.jpg",cv2.IMREAD_GRAYSCALE)

# our classifier returns the ROI of the detected face as a tuple
# It stores the top left coordinates & the bottom right coordinates
if face_classifier.empty():
    print("file couldn't load")
else:
    faces = face_classifier.detectMultiScale(image,1.3,5)
    print(faces)

# when no faces detected, face_classifier returns an empty face
#if faces is ():
#    print("no face found")

# we iterate through our faces array & draw a rectangle
# over each face in faces
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("face detection",image)
        cv2.waitKey(0)

cv2.destroyAllWindows()