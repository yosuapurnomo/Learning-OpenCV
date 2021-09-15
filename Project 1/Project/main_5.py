# PerspectiveTransform
import cv2
import numpy as np

img = cv2.imread("../Resource/cards.jpg")

width, height = 250, 350
pts1 = np.float32([[111,219], [287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0], [width,0], [0, height], [width, height]])

# cv2.line(img, (111, 219), (287, 188), (255,0,0))
# cv2.line(img, (154,482), (352,440), (0,0,0))
# cv2.line(img, (0,0), (width,0), (0,255,0))
# cv2.line(img, (0, height), (width, height), (0, 0, 255))

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
# imgCrop = img[219:482, 111:352]

print(matrix)

cv2.imshow("Image", img)
# cv2.imshow("Image Crop", imgCrop)
cv2.imshow("Image Output", imgOutput)

cv2.waitKey(0)
