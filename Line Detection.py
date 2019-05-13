import cv2
import numpy as np


imgpath2 = "/Users/rajatbhalla/Downloads/sudoku.jpeg"
img = cv2.imread(imgpath2)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges =  cv2.Canny(gray,100,170,apertureSize=3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)

for rho,theta in lines[0]:

    a=np.cos(theta)
    b=np.sin(theta)

    x0 = a * rho
    y0 = b * rho

    x1 = int(x0 + 1000 * (-b))
    x2 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (-a))
    y2 = int(y0 + 1000 * (-a))
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)



cv2.imshow('Hough Lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
