import numpy as np
import cv2

original_image = cv2.imread("../Data Testing/bird.jpg")

kernel = np.array([[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]])

Sharp_image = cv2.filter2D(original_image, -1, kernel)

cv2.imshow("Original Image", original_image)
cv2.imshow("Sharp Image", Sharp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()