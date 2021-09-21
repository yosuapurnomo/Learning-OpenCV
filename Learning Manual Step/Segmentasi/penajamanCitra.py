import numpy as np
import cv2
import matplotlib.pyplot as plt

class konvolusi:
    def __init__(self, image, kernel):
        self.image = image
        self.kernel = kernel
        # self.proses()

    def proses(self):
        newImage = np.zeros_like(self.image)
        x_akhir = x_kernel = y_akhir = y_kernel = len(self.kernel) // 2
        x_awal = y_awal = 0
        array = 0
        for y in range(self.image.shape[0]):
            if y >= len(self.kernel) // 2:
                y_awal = y - len(self.kernel) // 2
            else:
                y_awal = 0
            if y_akhir + 1 < self.image.shape[0]:
                y_akhir = y + len(self.kernel) // 2
            for x in range(self.image.shape[1]):
                if x >= len(self.kernel) // 2:
                    x_awal = x - len(self.kernel) // 2
                yKernel_copy = y_kernel
                for i in range(y_awal, y_akhir + 1):
                    xKernel_copy = x_kernel
                    for j in range(x_awal, x_akhir + 1):
                        array += self.kernel[yKernel_copy][xKernel_copy] * self.image[i][j]
                        xKernel_copy += 1
                    yKernel_copy += 1
                if x_akhir + 1 < self.image.shape[1]:
                    x_akhir = x + len(self.kernel) // 2
                if (x + 1) <= len(self.kernel) // 2:
                    x_kernel = x_kernel - 1
                if x + 1 >= self.image.shape[1]:
                    x_awal = 0
                    x_akhir = len(self.kernel) // 2
                    x_kernel = len(self.kernel) // 2
                newImage[y][x] = int(array/9)
                # if int(array) == 0:
                #     print(f"Y : {y} X : {x} q : {int(array)}")
                array = 0

            if y + 1 <= len(self.kernel) // 2:
                y_kernel -= 1
        return newImage

def grayscale(image):
    newImage = np.zeros((image.shape[0], image.shape[1]))
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            newImage[y][x] = (int(image[y][x][2]) + int(image[y][x][1]) + int(image[y][x][0])) / 3
    return np.array(newImage, dtype=np.uint8)


image = cv2.imread("../../Image data Testing/Dalam Ruangan Lampu.jpg")
grayImage = grayscale(image)

kernel1 = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

kernel2 = np.array([[1, 1, 1],
                   [0, -7, 0],
                   [1, 1, 1]])

image1 = cv2.filter2D(grayImage, -1, kernel1)
image2 = konvolusi(image1, kernel2/9)
image2 = image2.proses()
print(kernel2 / 9)
# image2 = cv2.filter2D(image1, -1, kernel2)
figure, axes = plt.subplots(1, 4, figsize=(15, 6))

axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title("Image Original")

axes[1].imshow(image1, "gray")
axes[1].set_title("Image 1")

axes[2].imshow(image2, "gray")
axes[2].set_title("Image 2")

axes[3].imshow(image2[145:165,170:250], "gray")
axes[3].set_title("Potong Image 2")

plt.show()