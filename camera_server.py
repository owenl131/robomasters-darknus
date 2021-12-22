from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import redis
import serialize

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
    image = frame.array
    frames.append(image)
    rawCapture.truncate(0)
    r.set('output', serialize.serialize(image))
    # if i == 300:
    #     break

cv2.imwrite('output.png', frames[-1])
elapsed = time.time() - start

print('elapsed', elapsed)
print('per frame', elapsed / 1000)
print('FPS', 1 / (elapsed / 1000))

