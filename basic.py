import cv2 as cv

img = cv.imread('media/image.jfif') #it is the matrix of the given image
cv.imshow('Profile', img)

#converting image into grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#bluring an image
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

#Edge cascade
canny = cv.Canny(blur, 125,175)
# cv.imshow('Canny edge',canny)

#Dilating an image
dilate = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilate)

#Eroding
eroded = cv.erode(dilate, (3,3), iterations=1)
# cv.imshow("Eroded", eroded)

#resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resize)

resize_up = cv.resize(img, (1920,1080), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resize_up)

#CROPPING
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
