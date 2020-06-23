import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import pyqtSlot, Qt, QDateTime
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtMultimedia import (QCameraInfo, QCameraImageCapture, QImageEncoderSettings,
                                QMultimedia, QVideoFrame, QSound, QCamera)
from ui import Ui_MainWindow
import cv2
import time

people = {"杨剑": "1811082011", "王萧行": "1911082188"}


class QmyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.camera = QCamera()
        cameras = QCameraInfo.availableCameras()
        if len(cameras) > 0:
            self.__iniCamera()
            self.__iniImageCapture()
            self.camera.start()

    def __iniCamera(self):
        cameraInfo = QCameraInfo.defaultCamera()
        self.camera = QCamera(cameraInfo)
        self.camera.setViewfinder(self.ui.PreviewWidgt)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)

    def __iniImageCapture(self):
        self.capture = QCameraImageCapture(self.camera)
        settings = QImageEncoderSettings()
        settings.setCodec("image/jpeg")
        settings.setResolution(640, 480)
        settings.setQuality(QMultimedia.HighQuality)
        self.capture.setEncodingSettings(settings)

        dest = QCameraImageCapture.CaptureToFile
        self.capture.setCaptureDestination(dest)

        self.capture.imageCaptured.connect(self.do_imageCaptured)

    @pyqtSlot()
    def on_actCapture_triggered(self):
        self.camera.searchAndLock()
        self.capture.capture()
        self.camera.unlock()
        # H = self.ui.ShowPhoto.height()
        # W = self.ui.ShowPhoto.width()

    @pyqtSlot()
    def on_actStartCamera_2_triggered(self):
        self.camera.start()

    @pyqtSlot()
    def on_actCloseCamera_triggered(self):
        self.camera.stop()

    def do_imageCaptured(self, imageID, preview):
        H = self.ui.ShowPhoto.height()
        W = self.ui.ShowPhoto.width()
        scaledImage = preview.scaled(W, H, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # self.ui.ShowPhoto.setPixmap(QPixmap.fromImage(scaledImage))
        # print(scaledImage.format())
        scaledImage.save("test.jpg")
        time_start = time.time()
        image = cv2.imread("test.jpg")
        faceCascade = cv2.CascadeClassifier(
            'data/haarcascades_cuda/haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(5, 5))
        # print("find {0} faces!".format(len(faces)))
        for(x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)
        cv2.imwrite("test.jpg", image)
        scaledImage = QImage()
        scaledImage.load("test.jpg")
        self.ui.ShowPhoto.setPixmap(QPixmap.fromImage(scaledImage))
        time_end = time.time()
        run_time = time_end - time_start
        # self.ui.editID.setText("1811082011")
        key = "杨剑"
        self.ui.editName.setText(key)
        self.ui.editID.setText(people[key])
        self.ui.editTime.setText(str(run_time) + 's')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyWindow()
    form.show()
    sys.exit(app.exec_())
