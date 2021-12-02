from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import detector
import redis
import serialize 

r = redis.Redis()

def main():
    resolution = (640, 480)
    camera = PiCamera()
    camera.resolution = resolution
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=resolution)

    time.sleep(0.1)
    start = time.time()
    frames = []
    try:
        for i, frame in enumerate(camera.capture_continuous(
                rawCapture, format='bgr', use_video_port=True)):
            image = frame.array
            frames.append(image)
            result = detector.detect(image)
            r.set('cap', serialize.serialize(result))
            rawCapture.truncate(0)
    except Exception as e:
        print(e)

    cv2.imwrite('output.png', frames[-1])
    elapsed = time.time() - start

    print('elapsed', elapsed)
    print('per frame', elapsed / 1000)
    print('FPS', 1 / (elapsed / 1000))


if __name__ == '__main__':
    main()
