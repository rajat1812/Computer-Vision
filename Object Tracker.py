import cv2
import numpy as np


cam = cv2.VideoCapture(0)

lower = np.array([130,50,90])
upper = np.array([170,255,255])

# Create empty points array
points =[]

# Get default camera window size
ret, frame = cam.read()
heigth ,width = frame.shape[:2]
frame_count = 0

while True:

    ret, frame = cam.read()
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only required colors
    mask = cv2.inRange(hsv_image,lower,upper)

    # Find contours
    contours , _  = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create empty center array to store centroid center of mass
    center = int(heigth/2), int(width/2)

    if len(contours) > 0:
       # Get the  largest contour & its center
        c = max(contours,key=cv2.contourArea)
        (x,y), radius = cv2.minEnclosingCircle(c)
        #print("x,y,radius",x,y,radius)

        M = cv2.moments(c)
        #print("Moments",M)

        try:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            print("center",center)
        except:
            center = int(heigth/2), int(width/2)

        # Allow contours that have a larger than 15 pixel
        if radius > 25:
            # Draw circle & leave the last center creating the trail
            cv2.circle(frame, (int(x),int(y)),int(radius),(0,0,255),2)
            cv2.circle(frame,center ,5 ,(0,255,0),-1)

        # Log center points
        points.append(center)
        print(points)

        # Loop over the  set of tracked points
        if radius > 25:
            for i in range(1,len(points)):
                try:
                    cv2.line(frame,points[i - 1],points[i],(0,255,0),2)
                except:
                    pass

        else :
            # Count frames
            frame_count += 1


            # If we count 10 frames without objectlets delete our trail
            if frame_count == 10:
                points = []
                # When frame_count reaches 20 lets clear out trail
                frame_count = 0



    # Display our object tracker
    frame = cv2.flip(frame,1)
    cv2.imshow("frame",frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()