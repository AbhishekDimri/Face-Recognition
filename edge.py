import cv2 as cv
import numpy as np

img = cv.imread('media/scene.jpg')
# cv.imshow('Profile', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Lap Lacion
Lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(Lap))
cv.imshow("Lap Lacion", lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

# cv.imshow('Sobel X', sobelx)
# cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

#Canny edge
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)
