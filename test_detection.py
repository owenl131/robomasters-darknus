from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import numpy as np
import redis
import serialize

def process_image(img):
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
            param1=50, param2=40, minRadius=0, maxRadius=0)
    if circles is None:
        return img
    circles = np.round(circles[0, :]).astype('int')
    print(len(circles))
    for x, y, r in circles:
        print(x, y, r)
        cv2.circle(img, (x, y), r, (0, 255, 0), 4)
    return img

resolution = (640, 480)
camera = PiCamera()
camera.resolution = resolution
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=resolution)
r = redis.Redis()
time.sleep(0.1)
start = time.time()
frames = []

for i, frame in enumerate(camera.capture_continuous(
        rawCapture, format='bgr', use_video_port=True)):
    image = frame.array.copy()
    image[:, :, 0] = 0
    image[:, :, 2] = 0
    image = process_image(image)
    r.set('cap', serialize.serialize(image))
    # frames.append(image)
    rawCapture.truncate(0)
    if i == 1000:
        break

# cv2.imwrite('output.png', frames[-1])
elapsed = time.time() - start

print('elapsed', elapsed)
print('per frame', elapsed / 1000)
print('FPS', 1 / (elapsed / 1000))

