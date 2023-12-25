import cv2 as cv

img = cv.imread('media/scene.jpg') #it is the matrix of the given image
cv.imshow('Profile', img)

#Averging
average = cv.blur(img,(3,3))
cv.imshow('Average blur',average)

#Gausian Blur
gauss = cv.GaussianBlur(img, (3,3),0)
cv.imshow('Gaussian', gauss)

#median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#Bilateral Blurring
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)