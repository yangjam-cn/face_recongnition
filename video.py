import cv2


def getPhoto():
    camera = cv2.VideoCapture()
    Image = cv2.imread('ORL/s1_5.bmp')
    while camera.isOpened():
        ret, Image = camera.read()
    return Image
