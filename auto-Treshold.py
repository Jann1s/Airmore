import cv2
import numpy as np
cv2.namedWindow("preview")
cameraID = 0
#Uncomment if running on the pi with the camera
#vc = cv2.VideoCapture(cameraID)
vc = cv2.imread('1.jpg')
frame = vc
#if vc.isOpened(): # try to get the first frame
 #   rval, frame = vc.read()
#else:
 #   rval = False

while 1==1:
    frame_v = cv2.applyColorMap(cv2.imread('1.jpg', 0), cv2.COLORMAP_HSV)
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
    # detect circles in the image
    img = cv2.COLOR_RGB2GRAY
    #img = cv2.convertScaleAbs(img)
    #img = cv2.convertScaleAbs(img, alpha=(255.0 / 65535.0))
    #contours, hierarchy, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #print(contours)
    #cv2.drawContours(img, contours, 0, (0, 255, 0), 3)
    #cv2.drawContours(img, [contours], 0, (0,255,0), 3)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=200, param2=100, minRadius=2, maxRadius=70)

    # circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 100)
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        print "fas"
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(img, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

        # show the output image
        cv2.imshow("output", np.hstack([img, img]))
        cv2.waitKey(0)
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    cv2.imwrite('testcircle.jpg', img)
    #########
    #Display image
    cv2.imshow("test", edges)
    cv2.imshow("preview",img)
    #rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break