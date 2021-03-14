import cv2

input = cv2.imread('image1.bmp')
# input = cv2.imread('image.jpg')

height, width = input.shape[:2]
# print(height, width )
w, h = (18,18)

temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR_EXACT    )
# print(len(temp))
f = []
f.append(temp)
print((temp))
print(type(f))
# print(f)
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
# print(output)
cv2.imshow('Input :', input)
cv2.imshow('Output :', output)
# print(input)
cv2.waitKey(0)

# cv2.imshow('Input :', input)
# cv2.imshow('Output :', output)

# print(cv2.resize)













