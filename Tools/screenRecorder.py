# pip install opencv-python
# pip install pyautogui

import pyautogui
import cv2
import numpy as np

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"CLCO") # ?? parece que la codificación está fallando

filename = "Tools/Recording.mp4"
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 370)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("Live", frame)
    if cv2.waitKey(1) == ord("q"):
        break

print("Screen Recorder Started")
out.release()
cv2.destroyAllWindows()
