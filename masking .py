import cv2 as cv
import numpy as np

img = cv.imread('media/scene.jpg') #it is the matrix of the given image
cv.imshow('Profile', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2 + 45), 100, 255, -1)
# cv.imshow('Mask', mask)
#
# masked = cv.bitwise_and(img, img, mask=mask)
# cv.imshow('Masked Image', masked)


circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2 + 45), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
weird_shape = cv.bitwise_or(circle, rectangle)
cv.imshow('Weird', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('weird shape Masked Image', masked)

cv.waitKey(0)