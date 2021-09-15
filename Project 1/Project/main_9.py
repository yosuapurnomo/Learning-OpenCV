import cv2

faceCascade = cv2.CascadeClassifier("../Resource/haarcascade_frontalface_default.xml")

img = cv2.imread('../Resource/people.jpg')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.2, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), ((x+w), (y+h)), (255,0,0), 2)

imgResize = cv2.resize(img, (0,0), None, 0.5, 0.5)
cv2.imshow("Result", imgResize)
cv2.waitKey(0)