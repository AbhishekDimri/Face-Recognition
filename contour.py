import cv2 as cv
import numpy as np

img = cv.imread('media/scene.jpg') #it is the matrix of the given image
cv.imshow('Profile', img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

#blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# canny1 = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny1)
# contours1, hierarchy1 = cv.findContours(canny1, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours1)} contour(s) found')

# ret, thresh = cv.threshold(gray, 125, 125, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)
# contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('Conours Drawn', blank)

cv.waitKey(0)
