import numpy as np

class grayscale:
    def __init__(self, image):
        self.image = image
        print(image.shape)
    def grayScale(self):
        newImage = np.zeros((self.image.shape[0], self.image.shape[1]))
        for y in range(self.image.shape[0]):
            for x in range(self.image.shape[1]):
                newImage[y][x] = (int(self.image[y][x][2]) + int(self.image[y][x][1]) + int(self.image[y][x][0])) / 3
        return np.array(newImage, dtype=np.uint8)