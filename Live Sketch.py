import cv2
import numpy as np

def sketch(image):

    # Sketch generating function

    image_gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

    image_blur = cv2.GaussianBlur(image_gray,(5,5),0)

    canny_edges = cv2.Canny(image_blur,10,70)

    ret ,frame = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return frame


cap = cv2.VideoCapture(0)

while True :

    ret, frame = cap.read()

    cv2.imshow("Live Sketch",sketch(frame))

    if cv2.waitKey(1) == 27:
         break


cv2.destroyAllWindows()
cap.release()



