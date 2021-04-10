import cv2
import numpy as np
a = np.array([[0, 1, 2, 3, 4, 5],[6, 7, 100, 9, 10, 11],[12, 13, 14, 15, 16, 17],[18, 19, 20, 21, 22, 23],[24, 25, 26, 27, 28, 29],[30, 31, 32, 33, 34, 35]], dtype=np.uint8)
print(a,end="\n\n")
print(cv2.resize(a, (5,5), interpolation=cv2.INTER_LINEAR_EXACT))