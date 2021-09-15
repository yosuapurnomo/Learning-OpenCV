# Resize and Cropping
import cv2

img = cv2.imread("../Resource/lambo.png")
print(img.shape)

imgResize = cv2.resize(img, (0,0), None, 0.5, 0.5 )
print(imgResize.shape)

imgCrop = img[0:200,200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Crop", imgCrop)

cv2.waitKey(0)