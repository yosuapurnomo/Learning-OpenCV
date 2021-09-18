import numpy as np
import cv2

def penempatan_garis(image, lines):
    # membuat gambar kosong / hitam untuk templates penempatan pola garis sementara
    lines_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    for line in lines:
        # x1 = titik lebar awal
        # y1 = titik tinggi awal
        # x2 = titik lebar akhir
        # y2 = titik tinggi akhir
        for x1, y1, x2, y2 in line:
            # cv2.line(gambar kosong / hitam, (titik lebar awal, titik tinggi akhir), (titik lebar akhir, titik tinggi akhir), (warna dalam RGB), ketebalan garis)
            cv2.line(lines_image, (x1, y1), (x2, y2), (255, 0, 0), thickness=3)
    # cv2.addWeighted(gambar asli, alpha, gambar templates garis, beta, gamma)
    image_with_line = cv2.addWeighted(image, 0.8, lines_image, 0.8, 0, )

    return image_with_line

def pemotongan_pola(image, pointer):
    # membuat gambar kosong / hitam dengan size yang sama dengan gambar asli
    mask = np.zeros_like(image)
    # cv2.fillPoly(gambar kosong/hitam, titik letak yang tlah ditentukan, warna(255=putih)
    # hasilnya akan menjadi gambar hitam dan putih dimana putih dihasilkan dari pola yang sudah ditentukan pada titik_segitiga
    cv2.fillPoly(mask, pointer, 255)
    # cv2.bitwise_and(gambar asli, gambar pola yang sudah ditentukan sebelumnya)
    # untuk menggabungkan gambar asli dengan pola diperlukan operasi AND
    # yang dimana jika 0(hitam | 0 0 0 0 0) and 1(jumlah bit pada pisex | 1 0 1 0 1) maka akan menghasilkan 0 (hitam | 0 0 0 0 0) yang akan dianggap false
    # jika 1(jumlah bit pada pisex | 1 0 1 0 1) and 1(putih) maka akan menghasilkan jumlah bit pisex yang sesuai | 1 0 1 0 1
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def deteksi_garis(image):
    (tinggi, lebar) = (image.shape[0], image.shape[1])

    # Konvulusi Gambar keabu-abuan
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Konvulusi Gambar Deteksi Tepi / Canny
    canny_image = cv2.Canny(gray_image, 100, 120)

    titik_segitiga = [
        (0, tinggi),
        (lebar/2, tinggi*0.65),
        (lebar, tinggi)
    ]

    cropped_image = pemotongan_pola(canny_image, np.array([titik_segitiga], np.int32))

    # cv2.HoughLinesP(hasil gambar yang tlah dipotong, rho, theta, ambang batas, minimal lebar garis, maximal ketebalan garis)
    # Hough Algorithm berfungsi untuk mendeteksi garis pada sebuah citra
    # https://docs.opencv.org/master/d6/d10/tutorial_py_houghlines.html untuk penyelasan teori lebih jelasnya
    line_detect = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi/180, threshold=50,
                                  lines=np.array([]), minLineLength=40, maxLineGap=150)

    line_image = penempatan_garis(image, line_detect)
    return line_image

video = cv2.VideoCapture("../Data Training/lane_detection_video.mp4")

while video.isOpened():
    akhir, frame = video.read()

    if not akhir:
        break

    frame = deteksi_garis(frame)
    cv2.imshow("View", frame)
    cv2.waitKey(20)

video.release()
cv2.destroyAllWindows()
