import cv2
import numpy as np

file_path = '../Sample_videos/sample2.gif'
cap = cv2.VideoCapture(file_path)
first_iteration = True
result = None

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    if first_iteration:
       avg = np.float32(frame)
       first_iteration = False

    cv2.accumulateWeighted(frame, avg, 0.005)

    result = cv2.convertScaleAbs(avg)

cv2.imshow("Result from running average", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

