import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("IMG_0183.JPG"))

if img is None:
    sys.exit("Could not read the image.")

dimensions = img.shape
print(dimensions)

percent = float(input("Reduce the quality of image to??? "))
percent = int(percent)

x = int((percent/100)*dimensions[1])
y = int((percent/100)*dimensions[0])

dsize = (x,y)

res = cv.resize(img,dsize,interpolation = cv.INTER_AREA)

cv.imshow('Reduced',res)
cv.waitKey(0)
cv.destroyAllWindows()