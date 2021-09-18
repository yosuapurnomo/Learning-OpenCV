import cv2
import matplotlib.pyplot as plt

cascade_class = cv2.CascadeClassifier("../Data Testing/haarcascade_frontalface_alt.xml")

# Opencv akan membaca pixel BGR, sedangkan Matplotlib membaca pixel RGB
image = cv2.imread("../Data Testing/Person_girl.jpg")

# Perlu menconvert dari Pixel BGR ke RGB
RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(RGB_image, cmap="gray")
plt.show()