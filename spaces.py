import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('media/scene.jpg') #it is the matrix of the given image
cv.imshow('Profile', img)

# plt.imshow(img)
# plt.show()

#convert it into the gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# BGR TO HSV (Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('Hsv', hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()

#HSV TO BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('HSV2BGR', hsv_bgr)

#LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB2BGR', lab_bgr)

cv.waitKey(0)