import cv2
import numpy as np
cv2.namedWindow("preview")
cameraID = 0
#Uncomment if running on the pi with the camera
#vc = cv2.VideoCapture(cameraID)
vc = cv2.imread('testpicture1.jpg')
frame = vc
#if vc.isOpened(): # try to get the first frame
 #   rval, frame = vc.read()
#else:
 #   rval = False

while 1==1:
    frame_v = cv2.applyColorMap(cv2.imread('testimage.png', 0), cv2.COLORMAP_HSV)
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
    #img = cv2.COLOR_RGB2GRAY
    #img = cv2.convertScaleAbs(img)
    contours, hierarchy, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(edges, contours, -1, (0, 255, 0), 3)
    #cv2.drawContours(img, [contours], 0, (0,255,0), 3)
    cv2.imwrite('testcountour.jpg', edges)
    ##########
    #Display image
    #cv2.imshow("preview", cv2.resize(cv2.cvtColor(mask * edges, cv2.COLOR_GRAY2RGB) | frame, (640, 480), interpolation=cv2.INTER_CUBIC))
    #rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break