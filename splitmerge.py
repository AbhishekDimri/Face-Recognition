import cv2 as cv
import numpy as np

img = cv.imread('media/scene.jpg') #it is the matrix of the given image
cv.imshow('Profile', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)
#
# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)
#
# merged = cv.merge([b,g,r])
# cv.imshow('Merged', merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow('Blue1', blue)
cv.imshow('Green1', green)
cv.imshow('Red1', red)

cv.waitKey(0)