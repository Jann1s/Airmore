import numpy as np
import argparse
import glob
import cv2
import sys
#function that draws the smallest circle enclosing the contour

def draw_Cirles(contour):
    (x, y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    print radius
    if(radius > 30 and radius <180):
        cv2.circle(image, center, radius, (0, 255, 0), 2)
        contour_list.append(contour)

def threshold(threshold, minusValue, image):
    # define the list of boundaries (pixel color)
    boundaries = [
        ([threshold - minusValue, threshold - minusValue, threshold - minusValue], [255, 255, 255])  # TODO: adjust threshold accordingly!!!
    ]
    # Loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        return output

def processImage(image):
    #threshold(maxVal,80)
    # Apply bilateral filtered image
    bilateral_filtered_image = cv2.bilateralFilter(image, 5, 175, 175)
    cv2.imshow("bilateral", bilateral_filtered_image)
    # Canny edge magic
    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
    cv2.imshow("Canny", edge_detected_image)
    return edge_detected_image

def findContours(image):
    # Now lets find the countors
    _, contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Sexy loop combined with approxPolyDP
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        area = cv2.contourArea(contour)
        draw_Cirles(contour)
        # if ((len(approx) > 8) & (len(approx) < 23) & (area > 6000) & (area < 99999) ):
        # print area
        # contour_list.append(contour)
def findMinMaxLoc(image,blurRadius):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (blurRadius, blurRadius), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    print maxVal
    copy = image.copy()
    cv2.circle(copy, maxLoc, 45, (255, 0, 0), 2)
    # display the results
    cv2.imshow("Robust", gray)
    return minVal,maxVal
contour_list = []
image =  cv2.resize(cv2.imread('iot6.png'),(640,480))
cv2.imshow("original",image)
# apply a Gaussian blur to the image then find the brightest region
minVal,maxVal = findMinMaxLoc(image,49)
processedImage = processImage(threshold(maxVal,90,image))
contours = findContours(processedImage)
cv2.drawContours(image, contour_list,  -1, (0,255,0), 2)
if(len(contour_list) > 0):
    print(str(len(contour_list)) + " persons were found in this picture")
    cv2.imshow("Result", image)
    cv2.waitKey(0)
else:
    cv2.imshow("Result", image)
    print("got nothing")
    cv2.waitKey(0)


