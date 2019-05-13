import cv2
import  numpy as np

imgpath = "/Users/rajatbhalla/Downloads/beach.jpeg"
image = cv2.imread(imgpath)
cv2.imshow("waldo beach",image)
cv2.waitKey(0)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


template_imgpath  = "/Users/rajatbhalla/Downloads/Tent.jpeg"
template_img = cv2.imread(template_imgpath,0)
cv2.imshow("waldo",template_img)
cv2.waitKey(0)

result = cv2.matchTemplate(gray,template_img,cv2.TM_CCOEFF)
min_val , max_cal , min_loc , max_loc = cv2.minMaxLoc(result)
print(min_val , max_cal , min_loc , max_loc )

top_left = max_loc
bottom_right = (top_left[0] + 100 , top_left[1] + 100)

cv2.rectangle(image,top_left,bottom_right,(0,0,255),5)
cv2.imshow('result',image)
cv2.waitKey(0)
cv2.destroyAllWindows()