
import cv2


imgpath = "/Users/rajatbhalla/Downloads/polygon-7-sides-heptagon-a4.jpg"
template_img = cv2.imread(imgpath)
resize_img1 = cv2.resize(template_img,(500,500))
template_gray = cv2.cvtColor(resize_img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('Template image', template_gray)
cv2.waitKey(0)

imgpath2 = "/Users/rajatbhalla/Downloads/polygons-made-with-illustrator.jpg"
target_img = cv2.imread(imgpath2)
target_gray = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(target_gray,30,200)



th = 127
max_val = 255

ret,thresh1 = cv2.threshold(template_gray,th,max_val,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(edged,th,max_val,cv2.THRESH_BINARY)



# Finding Contours
# Use a copy of your image edge.copy(), since find contours alters the image

contours, hierarchy= cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

sorted_contours = sorted(contours, key= cv2.contourArea,reverse=True)
#print( hierarchy)

#print('sorted_contours',sorted_contours)

#print('no. of contours found' , str(len(contours)))

template_contour =  contours[0]
c = cv2.moments(template_contour)
print('moment',c)
#print('template_contour',template_contour)

contours , hierarchy = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


# Iterate over our contours and draw one by one


for c in contours:

    match = cv2.matchShapes(template_contour,c,1,0.0)
    print("match",match)

    if match < 0.15:
        closest_counter = []
        closest_counter.append(c)

    else:
       pass




cv2.drawContours(target_img, closest_counter,-1, (0, 255, 0), 4)
cv2.imshow('contour image', target_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


