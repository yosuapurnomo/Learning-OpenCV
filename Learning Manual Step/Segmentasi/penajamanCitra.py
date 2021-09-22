import numpy as np
import cv2
import matplotlib.pyplot as plt

class gaussian:
    def __init__(self, image, size, sigma):
        self.image = image
        self.size = size
        self.sigma = sigma
        self.gaussian_kernel()

    def gaussian_kernel(self):
        size = int(self.size) // 2
        x, y = np.mgrid[-size:size + 1, -size:size + 1]
        normal = 1 / (2.0 * np.pi * self.sigma ** 2)
        self.kernel = np.exp(-((x ** 2 + y ** 2) / (2.0 * self.sigma ** 2))) * normal

    def gaussian_blur(self):
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
                        array += (self.kernel[yKernel_copy][xKernel_copy]/9) * self.image[i][j]
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
                newImage[y][x] = int(array)
                if int(array) == 0:
                    print(f"Y : {y} X : {x} q : {int(array)}")
                array = 0

            if y + 1 <= len(self.kernel) // 2:
                y_kernel -= 1
        return newImage

class konvolusi:
    def __init__(self, image, kernel):
        self.image = image
        self.kernel = kernel
        # self.proses()

    def proses(self):
        newImage = np.zeros_like(self.image, dtype=np.uint8)
        x_akhir = x_kernel = y_akhir = y_kernel = len(self.kernel) // 2
        x_awal = 0
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
                        array += (self.kernel[yKernel_copy][xKernel_copy] * self.image[i][j])
                        if array > 255:
                            array -= 255
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
                newImage[y][x] = array
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

image1 = cv2.filter2D(grayImage, 0, kernel1)
image2 = cv2.filter2D(image1, -1, kernel2)

potongan = image2[145:165,170:250]
(T, threshInv) = cv2.threshold(potongan, 90, 255, cv2.THRESH_BINARY)
print(image1[0:8, 0:8])
print(grayImage[0:8, 0:8])
figure, axes = plt.subplots(2, 3, figsize=(12, 6))

axes[0][0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0][0].set_title("Image Original")

# axes[1].imshow(imageGaussian, "gray")
# axes[1].set_title("Image 1")
axes[0][1].imshow(image1, "gray")
axes[0][1].set_title("Image 1")

axes[0][2].imshow(image2, "gray")
axes[0][2].set_title("Image 2")

axes[1][0].imshow(image2[145:165,170:250], "gray")
axes[1][0].set_title("Potong Image 2")

axes[1][1].imshow(threshInv, "gray")
axes[1][1].set_title("Threshold")

plt.show()