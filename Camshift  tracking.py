import cv2
import numpy as np

cam = cv2.VideoCapture(0)
# _,first_frame = cam.read()

x = 353
y = 455
h = 100
w = 100

image = cv2.imread('/Users/rajatbhalla/Downloads/roi_screenshot_25.03.2019.png')
# cv2.imshow('image',image)

# region of interest which is to track is cropped
roi = image[y:y + h, x:x + w]

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# create histogram
roi_hist = cv2.calcHist(hsv_roi, [0], None, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Configuration of Mean Shift
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

if cam.isOpened():
    ret, frame = cam.read()
    print(ret)
    print(frame)
else:
    ret = False

while ret:

    ret, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    print("hsv", hsv)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # apply camshift to track the new location
    ret, track_window = cv2.CamShift(mask, (x, y, w, h), term_criteria)
    x, y, w, h = track_window

    # we use polylines to represent adaptive window
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    cv2.polylines(frame, [pts], True, 255, 2)

    cv2.imshow('roi', roi)
    cv2.imshow('first_frame', image)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cam.release()


