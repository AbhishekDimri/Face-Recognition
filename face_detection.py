import cv2 as cv

#single chris
# img = cv.imread('media/chris.jpg')
# cv.imshow('Chris', img)
#
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # cv.imshow('Chris gray ', gray)
#
# haar_cascade = cv.CascadeClassifier('Haar_Cascade.xml')
#
# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
#
# print(f'Number of faces found = {len(faces_rect)}')
#
# for x,y,w,h in faces_rect:
#     cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
#
# cv.imshow('Detected Images', img)

#Multiple chris
img = cv.imread('media/chrises.jfif')
# cv.imshow('Hemsworth Evans Pratt ', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('chrises', gray)

haar_cascade = cv.CascadeClassifier('Haar_Cascade.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)
print(faces_rect)
print(f'Number of faces found = {len(faces_rect)}')

for x,y,w,h in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Images', img)

cv.waitKey(0)