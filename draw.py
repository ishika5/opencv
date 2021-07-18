import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')

cv.imshow('cat',img)

cv.waitKey(0)
cv.destroyAllWindow()