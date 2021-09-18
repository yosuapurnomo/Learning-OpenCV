import numpy as np


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
                newImage[y][x] = int(array)
                if int(array) == 0:
                    print(f"Y : {y} X : {x} q : {int(array)}")
                array = 0

            if y + 1 <= len(self.kernel) // 2:
                y_kernel -= 1
        return newImage
