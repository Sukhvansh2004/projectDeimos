import cv2
import numpy as np

class stitchedCamera:
    def __init__(self) -> None:
        self.streams = []
        self.codes = []

    def addCamera(self, cameraCode):
        self.streams.append(cv2.VideoCapture(cameraCode))

    def stitchCamera(self):
        # TODO
        pass

    def viewStream(self):
        ret, frame = self.streams[0].read()


cam1 = cv2.VideoCapture(1)
cam2 = cv2.VideoCapture(2)

while True:
    ret, frame = cam1.read()
    ret, frame2 = cam2.read()
    #cv2.imshow('cam1', frame)
    #cv2.imshow('cam2', frame2)
    #frame = cv2.rotate(frame, cv2.ROTATE_180)
    res = np.concatenate((frame, frame2), axis=1)
    cv2.imshow('conc', res)
    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.imwrite("src/vision/scripts/images/image_cam1.jpg", frame)
        cv2.imwrite("src/vision/scripts/images/image_cam2.jpg", frame2)
        break

cam1.release()
cam2.release()
cv2.destroyAllWindows()