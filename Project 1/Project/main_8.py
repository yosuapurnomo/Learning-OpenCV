import cv2
import numpy as np
from concat import stackImages


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt0 = contours[0]
    counter = 0
    # area0 = cv2.contourArea(cnt0)
    # M = cv2.moments(cnt0)
    print(contours[5])
    print(len(contours[5]))
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print("Area = ", cnt[0])
        if area>500:
            counter +=1
            cv2.drawContours(imgBlank, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print("Peri = ", peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            # print("Approx = \n", approx)
            # print("Len Approx = ", len(approx))

            objCor = len(approx)

            x, y, w, h = cv2.boundingRect(approx)


            if objCor == 3: objType='Tri'
            elif objCor == 4:
                if (w/float(h)) > 0.50 and (w/float(h) < 1.05):
                    objType='Square'
                else:objType='Rextangle'
            else: objType='circel'

            # print("x = ", x)
            # print("y = ", y)
            # print("w = ", w)
            # print("h = ", h)

            cv2.rectangle(imgContours, (x, y), (x + w, y + h), (255, 255, 0), 3)

            # print("Rectangle = (x, y) : ", (x,y), "(x+w, y+h) : ", (x+w, y+h))

            cv2.rectangle(imgFinal, (x, y), (x + w, y + h), (255, 255, 0), 3)
            cv2.putText(imgFinal, objType, (x + (w // 2) - 15, y + (h // 2) + 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)

    # cv2.line(imgContours, (301, 448), (416, 563), (255, 0, 0))
    # print(counter)

img = cv2.imread('../Resource/shapes.png')


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (3,3),3)
imgCanny = cv2.Canny(imgGray, 10, 10)
imgBlank = np.zeros_like(img)
imgContours = imgCanny.copy()
imgFinal = img.copy()
getContours(imgCanny)

conImg = stackImages(0.6, [[img, imgGray, imgCanny], [imgContours, imgBlank, imgFinal]])

cv2.imshow("Original", conImg)
cv2.waitKey(0)