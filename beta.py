import numpy as np
import argparse
import glob
import cv2
import sys

image =  cv2.resize(cv2.imread('3.jpg'),(640,480))
# define the list of boundaries (pixel color)
boundaries = [
	([100, 100, 100], [255, 255, 255]) # TODO: adjust threshold accordingly!!!
]
# Loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)

# Apply bilateral filtered image
bilateral_filtered_image = cv2.bilateralFilter(output, 5, 175, 175)

# Canny edge magic
edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)

# Now lets find the countors
_, contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []

# Sexy loop combined with approxPolyDP 
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
        contour_list.append(contour)

# Draw contours based on the results from contours_list
cv2.drawContours(output, contour_list,  -1, (0,255,0), 2)
if(len(contour_list) > 0):
    print(str(len(contour_list)) + " persons were found in this picture")
    cv2.imshow("Result", output)
    cv2.waitKey(0)
else:
    print("got nothing")
