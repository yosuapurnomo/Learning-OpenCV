# Line, Rectangle, Circle, Text
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0,10), (img.shape[1],img.shape[0]), (0, 255, 0)) # line(matriks/gambar, (Titik Awal), (Titik Akhir), (Warna))
cv2.rectangle(img, (50, 20), (200, 200), (255,0,0), cv2.FILLED) # rectangle(matriks/gambar, (Titik Awal), (Titik Akhir), (warna), cv2.FILLED=border isi)
cv2.circle(img, (200,250), 30, (255, 255, 0), 1) # circle(matriks/gambar, (Titik tengah), (luas), (Warna), border size)
cv2.putText(img, "YOSUA", (150,330), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 2) # putText(matriks/gambar, "Text Input", (Titik Letak), cv2.FONT, sizeFont, (Warna), border)

cv2.imshow("Image", img)

cv2.waitKey(0)