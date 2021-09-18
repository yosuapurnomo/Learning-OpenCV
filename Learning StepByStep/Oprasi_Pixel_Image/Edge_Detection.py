import numpy as np
import cv2

original_image = cv2.imread("../Data Training/bird.jpg")

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Laplacian Kernel / Deteksi Tepi
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])

laplacian_Image = cv2.Laplacian(gray_image, -1)
result_image = cv2.filter2D(gray_image, -1, kernel)

cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Laplacian Image", laplacian_Image)
cv2.imshow("Result Image", result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()