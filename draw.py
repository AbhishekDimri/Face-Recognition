import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('blank', blank)

#paint in some colour
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

#painting certain part of the image
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

#Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
# cv.imshow('Rectangle', blank)

# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)
#
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

#Draw circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,250), thickness=3)
# cv.imshow('Circle', blank)

#Drwa a line
cv.line(blank, (250,250), (500,500), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

#Write a text
cv.putText(blank, 'Kite', (300,150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)