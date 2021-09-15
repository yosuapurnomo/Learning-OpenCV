import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
videoCapture = cv2.VideoCapture(0)
videoCapture.set(3, frameWidth)
videoCapture.set(4, frameHeight)
videoCapture.set(10, 150)

colorPick = [[25,90, 130, 179, 255, 255], # Kuning
             [0, 150, 135, 179, 255, 255], # Orange
             [15, 100, 150, 179, 255, 255]] # Biru

def findColor(img, colorPick):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in colorPick:
        lower = np.array(color[:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgContour, (x, y), 10, (255, 0, 255), cv2.FILLED)
        # cv2.imshow(str(color[0]), mask)

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

while True:
    success, img = videoCapture.read()
    imgContour = img.copy()
    findColor(img, colorPick)
    cv2.imshow("Resault", imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
