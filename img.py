import cv2 as cv
import numpy as np

img = cv.imread("github.png")
res = cv.resize(img,(300,300))
wind_name ='image'
h=np.hstack((res,res))
v=np.vstack((h,h))

cv.imshow(wind_name,v)
cv.waitKey(0)
cv.destroyAllWindows()