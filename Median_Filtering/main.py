import cv2
import numpy as np


file_path = '../Sample_videos/sample1.gif'
video = cv2.VideoCapture(file_path)

FOI = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)
frames = []

for frameOI in FOI:
    video.set(cv2.CAP_PROP_POS_FRAMES, frameOI)
    ret, frame = video.read()
    frames.append(frame)

result2 = np.median(frames, axis=0).astype(dtype=np.uint8)

cv2.imshow("Median filtering result",result2)
cv2.waitKey(0)
cv2.destroyAllWindows()