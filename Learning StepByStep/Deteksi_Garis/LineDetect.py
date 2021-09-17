import numpy as np
import cv2

def draw_line(image, lines):

    lines_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(lines_image, (x1, y1), (x2, y2), (255, 0, 0), thickness=3)

    image_with_line = cv2.addWeighted(image, 0.8, lines_image, 0.8, 0)

    return image_with_line

def region_crop(image, pointer):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, pointer, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def get_detected_lanes(image):
    (tinggi, lebar) = (image.shape[0], image.shape[1])

    # Konvulusi Gambar keabu-abuan
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Konvulusi Gambar Deteksi Tepi / Canny
    canny_image = cv2.Canny(gray_image, 100, 120)

    Triangle_pointer = [
        (0, tinggi),
        (lebar/2, tinggi*0.65),
        (lebar, tinggi)
    ]

    cropped_image = region_crop(canny_image, np.array([Triangle_pointer], np.int32))

    line_detect = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi/180, threshold=50,
                                  lines=np.array([]), minLineLength=40, maxLineGap=150)

    line_image = draw_line(image, line_detect)
    return line_image

video = cv2.VideoCapture("../Data Testing/lane_detection_video.mp4")

while video.isOpened():
    akhir, frame = video.read()

    if not akhir:
        break

    frame = get_detected_lanes(frame)
    cv2.imshow("View", frame)
    cv2.waitKey(50)

video.release()
cv2.destroyAllWindows()
