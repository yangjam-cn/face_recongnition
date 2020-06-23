import cv2
import numpy
print(cv2.__version__)
# image = cv2.imread("../images/132.bmp")
# cv2.imshow("test", image)
# cv2.waitKey(0)
arr = numpy.array([[1, 2, 3]])
a, b, c = arr[0, 0], arr[0, 1], arr[0, 2]
print(arr)
print(a)