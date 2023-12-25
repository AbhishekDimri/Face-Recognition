import cv2 as cv
import numpy as np

def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print('Area = ',area)
        cv.drawContours(imgContour, cnt, -1, (255,0,0), 3)
        if area > 500:
            perimeter = cv.arcLength(cnt, True)
            print('Perimeter = ',perimeter)
            approx = cv.approxPolyDP(cnt, 0.02*perimeter, True)
            print('Approx = ', len(approx))

            objCor = len(approx)
            x,y,w,h = cv.boundingRect(approx)
            if objCor == 3:
                objectType = 'Triangle'
            elif objCor == 4:
                aspectRatio = w/float(h)
                if (aspectRatio > 0.95) and (aspectRatio < 1.05):
                    objectType = 'Square'
                else:
                    objectType = 'Rectangle'
            elif objCor > 4:
                objectType = 'Circle'

            else:
                objectType = 'None'

            cv.rectangle(imgContour, (x,y),(x+w, y+h),(0,255,0), 3)
            cv.putText(imgContour, objectType,
                       (x+(w//2)-10, y+(h//2)-10), cv.FONT_HERSHEY_COMPLEX, 0.5,
                       (0,0,0), 2)




img = cv.imread('media/shapes.jpeg')
cv.imshow('Original', img)
imgContour = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(gray, (7,7), 1)

imgCanny = cv.Canny(imgBlur, 50,50)
# cv.imshow('Canny', imgCanny)

getContours(imgCanny)
cv.imshow('Contours', imgContour)

cv.waitKey(0)