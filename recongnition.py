import cv2
import numpy as np


# 利用cv2的LBPH识别器实现人脸识别
def testLBPH(face_image):
    images = list()
    images.append(cv2.imread('ORL/s1_1.bmp', cv2.IMREAD_GRAYSCALE))
    images.append(cv2.imread('ORL/s1_2.bmp', cv2.IMREAD_GRAYSCALE))
    images.append(cv2.imread('ORL/s2_1.bmp', cv2.IMREAD_GRAYSCALE))
    images.append(cv2.imread('ORL/s2_2.bmp', cv2.IMREAD_GRAYSCALE))
    images.append(cv2.imread('ORL/s3_1.bmp', cv2.IMREAD_GRAYSCALE))
    images.append(cv2.imread('ORL/s3_2.bmp', cv2.IMREAD_GRAYSCALE))
    lables = [1, 1, 2, 2, 3, 3]
    recongnizer = cv2.face.LBPHFaceRecognizer_create()
    recongnizer.train(images, np.array(lables))
    label, confidence = recongnizer.predict(face_image)
    return label, confidence


def get_face(image_gray):
    faceCascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(image_gray, scaleFactor=1.5, minNeighbors=5, minSize=(5,
                                                                                               5))
    if len(faces) == 1:
        x, y, w, h = faces[0, 0], faces[0, 1], faces[0, 2], faces[0, 3]
        image_face = image_gray[x:x+w, y:y+h]
        return image_face
    else:
        return None


def get_bit(image_gray, bit):
    r, c = image_gray.shape
    image_bit = np.zeros((r, c), dtype=np.uint8)
    image_bit = 2**bit
    image_bit = cv2.bitwise_and(image_gray, image_bit)
    return image_bit


# test
image = cv2.imread('images/ceshi.jpg', cv2.IMREAD_GRAYSCALE)
face = get_face(image)
bit_face = get_bit(face, 0)
mask = bit_face[:, :] > 0
bit_face[mask] = 255
cv2.imshow('test', bit_face)
cv2.waitKey(0)
cv2.destroyAllWindows()
