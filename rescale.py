import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #images, videos, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changesRes(width, height):
    #live video(web cam)
    capture.set(3,width)
    capture.set(4,height)


capture = cv.VideoCapture('media/video.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,0.2)
    cv.imshow('video', frame)
    cv.imshow('video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# img = cv.imread('media/image.jfif') #it is the matrix of the given image
# cv.imshow('Profile', img)
# img_resized = rescaleFrame(img,0.2)
# cv.imshow('Resized Image',img_resized)
# cv.waitKey(0)