import numpy as np
import cv2

original_image = cv2.imread('../Data Training/bird.jpg')

kernel = np.ones((5, 5)) / 20
print(kernel)

# -1 "Kedalaman Blur effect"
blur_image = cv2.filter2D(original_image, -1, kernel)

# Gaussian blur digunakan untuk mengurangi noise pada gambar

cv2.imshow("Original Image", original_image)
cv2.imshow("Blur Image", blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
