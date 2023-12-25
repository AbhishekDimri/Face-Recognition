import cv2 as cv
import numpy as np

def empty(a):
    pass

cv.namedWindow('TrackBars')
cv.resizeWindow('TrackBars', 640,240)
cv.createTrackbar('Hue Min', 'TrackBars', 0,179,empty)
cv.createTrackbar('Hue Max', 'TrackBars', 179,179,empty)
cv.createTrackbar('Sat Min', 'TrackBars', 0,255,empty)
cv.createTrackbar('Sat Max', 'TrackBars', 255,255,empty)
cv.createTrackbar('Value Min', 'TrackBars', 0,255,empty)
cv.createTrackbar('Value Max', 'TrackBars', 255,255,empty)

while True:
    img = cv.imread('media/mountain.jpg')
    cv.imshow('Profile', img)

    h_min = cv.getTrackbarPos('Hue Min', 'TrackBars')
    h_max = cv.getTrackbarPos('Hue Max', 'TrackBars')
    sat_min = cv.getTrackbarPos('Sat Min', 'TrackBars')
    sat_max = cv.getTrackbarPos('Sat Max', 'TrackBars')
    val_min = cv.getTrackbarPos('Value Min', 'TrackBars')
    val_max = cv.getTrackbarPos('Value Max', 'TrackBars')
    print(h_min, h_max, sat_min, sat_max, val_min, val_max)

    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])
    mask = cv.inRange(imgHSV, lower, upper)

    imgResult = cv.bitwise_and(img, img, mask=mask)
    # cv.imshow('Mask', mask)
    cv.imshow('Image result', imgResult)


    cv.waitKey(1)
