import cv2
import matplotlib.pyplot as plt

cascade_class = cv2.CascadeClassifier("../Data Training/haarcascade_frontalface_alt.xml")

video = cv2.VideoCapture("../Data Training/Face People.mp4")

while True:
    akhir, frame = video.read()

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    deteksi_wajah = cascade_class.detectMultiScale(gray_image, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    for (x, y, lebar, tinggi) in deteksi_wajah:
        cv2.rectangle(frame, (x, y), (x+lebar, y+tinggi), (255, 0, 0), 10)

    cv2.imshow("Deteksi Wajah", frame)
    key = cv2.waitKey(15) & 0xff
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()

