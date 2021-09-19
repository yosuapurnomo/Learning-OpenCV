import matplotlib.pyplot as plt
from skimage import data, feature
# skimage tlah menyediakan data yang dapat digunakan untuk proses training / pembelajaran

# Histogram of Oriented Gradients (HOG) ada beberapa step :
# - penghitungan pada gradient kernel
#       penghitungan menggunakan metode convolution dan memberikan kernel yang dimana :
#           Gambar -> representation dari matriks
#           kernel (ciri deteksi atau filter) -> bentuk matriks lainnya
#       bentuk gradient kernel : Gx = [-1, 0, 1] (Secara Horizontal)
#                                Gy =    [-1, (Secara Vertikal)
#                                          0,
#                                          1,]
#       jika dijadikan satu (Gxy) maka :
#                                           [-1,
#                                        [-1, 0, 1]
#                                             1]



image = data.astronaut()
print(image.shape)

hog_vektor, hog_image = feature.hog(image, orientations=9, cells_per_block=(2, 2), block_norm="L2", visualize=True)

figure, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(image)
axes[0].set_title("Original Image")

axes[1].imshow(hog_image)
axes[1].set_title("HOG Image")

plt.show()
