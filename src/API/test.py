import cv2 as cv
import numpy as np
import cv2
input = cv.imread('flo.png', cv.IMREAD_UNCHANGED)
height, width = input.shape[:2]
# print(height, width )
w, h = (10, 10)
t = [[[125,5,247],
     [102,19,181]],
     [[126,1,255],
      [126,1,254]]]
# t = [[[125,1,255],
#      [127,0,255]],
#      [[184,183,249],
#       [183,183,249]]]
arr = np.array(t)
temp = cv.resize(input, (w, h), interpolation=cv.INTER_LINEAR)
print(arr)
print(temp)

result = cv.matchTemplate(
    temp.astype(np.uint8),
    arr.astype(np.uint8),
    cv.TM_SQDIFF)
# print(result)
positions = np.argwhere(result == 0.0)

print(positions)