import cv2
import numpy as np
cv2.namedWindow("preview")
cameraID = 0
cap = cv2.imread('testimage.jpg', 0);
##vc = cv2.VideoCapture(cameraID)

##if vc.isOpened(): # try to get the first frame
    ##rval, frame = vc.read()
##else:
  ##  rval = False

while 1==1:
   ## frame_v = cv2.cvtColor(cap, cv2.COLOR_RGB2HSV)[:,:,2]

    blurredBrightness = cv2.bilateralFilter(cap,9,150,150)
    thresh = 50
    edges = cv2.Canny(blurredBrightness,thresh,thresh*2, L2gradient=True)

    _,mask = cv2.threshold(blurredBrightness,200,1,cv2.THRESH_BINARY)
    erodeSize = 5
    dilateSize = 7
    eroded = cv2.erode(mask, np.ones((erodeSize, erodeSize)))
    mask = cv2.dilate(eroded, np.ones((dilateSize, dilateSize)))
    detection = cv2.cvtColor(mask*edges, cv2.COLOR_GRAY2RGB)
    cv2.imshow("preview", cv2.resize(cv2.cvtColor(mask*edges, cv2.COLOR_GRAY2RGB) | cap, (640, 480), interpolation = cv2.INTER_CUBIC))
    ##rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
        #test
        