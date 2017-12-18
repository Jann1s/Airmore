# import the necessary packages
import numpy as np
import argparse
import cv2
import sys
# construct the argument parse and parse the arguments

# load the image
people_count = 0
image =  cv2.resize(cv2.imread('img2.jpg'),(640,480))
# define the list of boundaries (pixel color)
boundaries = [
	([165, 165, 165], [255, 255, 255])
]
# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
cimg= cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
	# show the images
# circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, 1, param1=50, param2=30, minRadius=0, maxRadius=0)  # 10 58
# if circles is None:
#     sys.exit('No circles found!')
# circles = np.uint16(np.around(circles))
# for i in circles[0, :]:
#     cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
#     people_count += 1;
#     print(people_count)
# cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
#
cv2.imshow('detected circles', output)
cv2.imshow("images", np.hstack([image, output]))
cv2.waitKey(0)