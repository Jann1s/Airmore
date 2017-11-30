# Grabbed from https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
# import the necessary packages
import numpy as np
import argparse
import glob
import cv2


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--images", required=True,
#                 help="path to input dataset of images")
# args = vars(ap.parse_args())
#
# # loop over the images
# for imagePath in glob.glob(args["images"] + "/*.jpg"):
# load the image, convert it to grayscale, and blur it slightly
while (1 == 1):
    image = cv2.applyColorMap(cv2.imread('testimage.png', 0), cv2.COLORMAP_HSV)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # apply Canny edge detection using a wide threshold, tight
    # threshold, and automatically determined threshold
    wide = cv2.Canny(blurred, 10, 200)
    tight = cv2.Canny(blurred, 225, 250)
    auto = auto_canny(blurred)

    # show the images
    im, contours, hierarchy = cv2.findContours(auto, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imshow("objects Found", image)
    cv2.imshow("Original", image)
    cv2.imshow("Edges", np.hstack([wide, tight, auto]))

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    cv2.waitKey(0)