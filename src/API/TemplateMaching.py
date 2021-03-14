
import numpy as np
import cv2 as cv

x = [[0, 0, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0]]

template = [[1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0]]

from scipy import signal

match = np.sum(template)
print(match)
# tst = signal.convolve2d(x, template[::-1, ::-1], mode='valid') == match
print(template[::-1, ::-1])
# candidates = np.argwhere(tst)