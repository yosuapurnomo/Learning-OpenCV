import cv2
import numpy as np
from gaussian_Blur import gaussian
from grayscale import grayscale
from gradient_Calculation import gradient

frame = cv2.imread('../Image data Testing/Girl_image.png')
frame = grayscale(frame)
gaussian = gaussian(frame.grayScale(), 5, 1.4)
gradientFrame = gradient(gaussian.gaussian_blur())
G, theta = gradientFrame.sobel_filters()
# print(G)
# cv2.imshow("Girl Gaussian", gaussian.gaussian_blur())
cv2.imshow("Girl Gradient Sobel", G)
cv2.imshow("Girl", frame.grayScale())
cv2.waitKey(0)
