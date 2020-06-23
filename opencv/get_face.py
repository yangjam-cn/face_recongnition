import cv2

faceCascade = cv2.CascadeClassifier('F:/source/python/FaceRecongnition/facerecongnition/data'
                                    '/haarcascades/haarcascade_frontalface_default.xml')
gray = cv2.imread('../images/ceshi.jpg', cv2.IMREAD_GRAYSCALE)
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(5, 5))
# print(len(faces), faces, faces[0:1])
x = faces[0, 0]
y = faces[0, 1]
w = faces[0, 2]
h = faces[0, 3]
face = gray[x:x+w, y:y+h]
cv2.imshow("test", face)
cv2.waitKey(0)
cv2.destroyAllWindows()

