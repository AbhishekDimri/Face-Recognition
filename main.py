import cv2 as cv

# img = cv.imread('media/image.jfif') #it is the matrix of the given image
# cv.imshow('Profile', img)


# cv.waitKey(0)

##################################################################
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

#################################################################
