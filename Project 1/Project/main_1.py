# Read Image, Video, Webcam
import cv2

# Image
# cap = cv2.imread('../Resource/lena.png') # Mengambil gambar
# cv2.imshow("Image", cap)
# cv2.waitKey(0)

# Video
cap = cv2.VideoCapture('../Resource/test_video.mp4') # Mengambil video melalui File mp4
# Webcam
# cap = cv2.VideoCapture(0) # Mengambil gambar melalui WebCam

# Functions Set hanya berfungsi untuk video/webcam
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 50)



# Menampilkan video harus dilakukan pengulangan untuk mengambil perFrame
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break