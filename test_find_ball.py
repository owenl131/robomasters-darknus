from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import serial_comm
import detector

def main():
    resolution = (640, 480)
    camera = PiCamera()
    camera.resolution = resolution
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=resolution)

    time.sleep(0.1)
    start = time.time()
    frames = []

    serial_comm.move('right')
    try:
        for i, frame in enumerate(camera.capture_continuous(
                rawCapture, format='bgr', use_video_port=True)):
            image = frame.array
            frames.append(image)
            detections, drawn = detector.detect(image)
            if len(detections) != 0:
                frames.append(drawn)
                print(len(detections))
                # print(detections)
                serial_comm.move('stop')
                break
            rawCapture.truncate(0)
            if i == 3000:
                break
            time.sleep(0.1)
    except Exception as e:
        print(e)
        serial_comm.move('stop')

    cv2.imwrite('output.png', frames[-1])
    elapsed = time.time() - start

    print('elapsed', elapsed)
    print('per frame', elapsed / 1000)
    print('FPS', 1 / (elapsed / 1000))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
