import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('Haar_Cascade.xml')
people = ['Evans', 'Hemsworth', 'Pratt']

features = np.load('features.npy', allow_pickle= 'True')
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('media\chrises.jfif')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 7)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {label} with a confidence = {confidence}')

    cv.putText(img, str(people[label]), (x,y), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0,255,0), thickness=2)

    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected image', img)
cv.waitKey(0)