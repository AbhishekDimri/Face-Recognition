import numpy as np
import cv2 as cv

img = cv.imread('media/scene.jpg') #it is the matrix of the given image
cv.imshow('Profile', img)

#Tranlation(shifting an image along x or y axis)
def translate(img, x,y):
    tranMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, tranMat, dimensions)

# -x ---> left
# -y ---> up
# +x ---> right
# +y ---> down

translated = translate(img, -100, -100)
# cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

# -angle ---> anticlockwise
# +angle ---> clockwise

rotated = rotate(img, 45)
# cv.imshow('Rotated', rotated)

rotated_further = rotate(rotated, 45)
# cv.imshow('Rotated further', rotated_further)

rotate_90 = rotate(img, 90)
# cv.imshow('Rotated_90', rotate_90)

#resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resize)

#Fliping
#0 ---> vertically
#1 ---> Horizontally
#-1 --> Both vertically and Horizontally

flip = cv.flip(img, 1)
# cv.imshow('Flipped', flip)

flip = cv.flip(img, -1)
# cv.imshow('Flipped', flip)

#croping
cropped = img[500:600, 300:400]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)

