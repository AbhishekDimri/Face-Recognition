import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('media/scene.jpg') #it is the matrix of the given image
cv.imshow('Profile', img)
#
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)

cv.imshow('masked', masked)
#
# gray_hist = cv.calcHist([gray],[0], masked, [256], [0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# colors = ('b', 'g', 'r')
# plt.figure()
# plt.title('color Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# for i,col in enumerate(colors):
#     hist = cv.calcHist([img], [i], None, [256], [0,256])
#     plt.plot(hist, color=col)
#     plt.xlim([0,256])
#
# plt.show()

#masked histogram for colour image

colors = ('b', 'g', 'r')
plt.figure()
plt.title('masked color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)