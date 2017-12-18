import cv2
import numpy as np
import sys

people_count= 0
cameraID = 0
#Uncomment if running on the pi with the camera
#vc = cv2.VideoCapture(cameraID)
vc = cv2.imread('img2.jpg')
frame = vc
#if vc.isOpened(): # try to get the first frame
 #   rval, frame = vc.read()
#else:
 #   rval = False

frame_v = cv2.applyColorMap(cv2.imread('img2.jpg', 0), cv2.COLORMAP_HSV)
blurredBrightness = cv2.bilateralFilter(frame_v,9,150,150)
thresh = 50
#Apply canny edge
edges = cv2.Canny(blurredBrightness,thresh,thresh*2, L2gradient=True)
_,mask = cv2.threshold(blurredBrightness,200,1,cv2.THRESH_BINARY)
erodeSize = 5
dilateSize = 7
eroded = cv2.erode(mask, np.ones((erodeSize, erodeSize)))
mask = cv2.dilate(eroded, np.ones((dilateSize, dilateSize)))
#Convert mask to gray otherwise it don't work
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
img = (cv2.cvtColor(mask * edges, cv2.COLOR_GRAY2RGB))
########## Lose all hope ye who enter
img = cv2.resize(cv2.cvtColor(mask * edges, cv2.COLOR_GRAY2RGB) | frame, (640, 480), interpolation=cv2.INTER_CUBIC)
#img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, 150, param1=50, param2=30, minRadius=4, maxRadius=60)#10 58
if circles is None:
    sys.exit('No circles found!')
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    people_count+=1;
    print(people_count)
cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()