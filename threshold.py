import cv2 as cv

img = cv.imread('media/scene.jpg')
# cv.imshow('Profile', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple threshlod', thresh)

# threshold1, thresh1 = cv.threshold(gray, 255//2, 255, cv.THRESH_BINARY)
# cv.imshow('Simple threshlod 1', thresh1)

# threshold_inv, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Simple threshlod inverse', thresh_inv)


#Adaptive thresholding
adavtive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Threhold', adavtive_thresh)

# adavtive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
# cv.imshow('Adaptive Threhold1', adavtive_thresh)

# adavtive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 5)
# cv.imshow('Adaptive Threhold2', adavtive_thresh)

# adavtive_thresh1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
# cv.imshow('Adaptive Threhold Gaussian', adavtive_thresh1)

# adavtive_thresh = cv.adaptiveThreshold(gray, 255, cv.CALIB_CB_ADAPTIVE_THRESH, cv.THRESH_BINARY, 11, 3)
# cv.imshow('Adaptive Threhold Calib', adavtive_thresh)

cv.waitKey(0)