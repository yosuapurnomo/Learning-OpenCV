import cv2
import numpy as np

img = cv2.imread('../Resource/lena.png')
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (9,9),1)

imgCanny = cv2.Canny(img, 150, 200)

imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

imgErode = cv2.erode(imgDialation, kernel, iterations=1)

print(kernel)
print("Dialations \n", imgDialation)
cv2.imshow("Image Gray", imgGray)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Dialation", imgDialation)
cv2.imshow("Image Erode", imgErode)



cv2.waitKey(0)