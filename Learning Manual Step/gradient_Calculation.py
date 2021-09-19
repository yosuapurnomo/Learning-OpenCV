import numpy as np
from scipy import ndimage

class gradient:
    def __init__(self, image):
        self.image = image
        self.Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
        self.Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

    def konvolusi(self, kernel):
        newImage = np.zeros_like(self.image)
        x_akhir = x_kernel = y_akhir = y_kernel = len(kernel) // 2
        x_awal = y_awal = 0
        array = 0
        for y in range(self.image.shape[0]):
            if y >= len(kernel) // 2:
                y_awal = y - len(kernel) // 2
            else:
                y_awal = 0
            if y_akhir + 1 < self.image.shape[0]:
                y_akhir = y + len(kernel) // 2
            for x in range(self.image.shape[1]):
                if x >= len(kernel) // 2:
                    x_awal = x - len(kernel) // 2
                yKernel_copy = y_kernel
                for i in range(y_awal, y_akhir + 1):
                    xKernel_copy = x_kernel
                    for j in range(x_awal, x_akhir + 1):
                        array += kernel[yKernel_copy][xKernel_copy] * self.image[i][j]
                        xKernel_copy += 1
                    yKernel_copy += 1
                if x_akhir + 1 < self.image.shape[1]:
                    x_akhir = x + len(kernel) // 2
                if (x + 1) <= len(kernel) // 2:
                    x_kernel = x_kernel - 1
                if x + 1 >= self.image.shape[1]:
                    x_awal = 0
                    x_akhir = len(kernel) // 2
                    x_kernel = len(kernel) // 2
                newImage[y][x] = int(array)
                # if int(array) == 0:
                #     print(f"Y : {y} X : {x} q : {int(array)}")
                array = 0

            if y + 1 <= len(kernel) // 2:
                y_kernel -= 1
        return newImage

    def sobel_filters(self):
        # Ix = self.konvolusi(self.Kx)
        # Iy = self.konvolusi(self.Ky)
        Ix = ndimage.filters.convolve(self.image, self.Kx)
        Iy = ndimage.filters.convolve(self.image, self.Ky)

        G = np.hypot(Ix, Iy)
        G = G / G.max() * 255
        theta = np.arctan2(Iy, Ix)
        image = np.array(G, dtype=np.uint8)
        return (image, theta)
