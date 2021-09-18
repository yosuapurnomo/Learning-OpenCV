import cv2
import matplotlib.pyplot as plt

cascade_class = cv2.CascadeClassifier("../Data Training/haarcascade_frontalface_alt.xml")

image = cv2.imread("../Data Training/people.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# scaleFactor = terkadang wajah yang terlalu dekat dengan kamera akan tampak lebih besar dari wajah yang lainnya
# ini menentukan seberapa besar ukuran gambar dikurangi pada setiap skala gambar
# Value = 1.1 - 1.4
# jika value kecil maka algoritma pencarian akan berjalan lambat dan jika value besar maka algoritma pencarian akan berjalan cepat
# namun jika menggunakan value yang besar untuk mendapatkan proses yang cepat, ini akan beresiko pada lolosnya/hilangnya pencarian wajah lainnya
# jadi inilah yang menyebabkan adanya perbedaan kecepatan algoritma dan keakuratan algoritma

# minNeighbors = berfungsi untuk menspesifikasikan berapa banyak ketetanggaan setiap kandidat yang ditemukan
# semakin besar value maka lebih sedikit terdeteksi tetapi dengan kualitas yang lebih tinggi
# jadi inilah yang berpengaruh pada lamanya proses dan kualitas pencarian yang dapat terdeteksi
# jika menggunakan value kecil seperti 0 maka kemungkinan akan mendapatkan deteksi positif false
# yang dimana hali ini dapat digunakan untuk mentraining / mengklarifikasikan akurasi dari hasil tersebut

# minSize = berfungsi untuk menspesifikasikan berapa minimal ukuran kotak deteksi pada sebuah objects
# [30 x 30] ini adalah ukuran standar

# maxSize = berfungsi untuk menspesifikasikan berapa maximal ukuran kotak deteksi pada sebuah objects
cascade_image = cascade_class.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=10, minSize=(30, 30))

for (x, y, lebar, tinggi) in cascade_image:
    cv2.rectangle(image, (x, y), (x+lebar, y+tinggi), (255, 0, 0), 5)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()