from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import serial_comm
import detector
import serialize
import redis
import robot

rob = robot.Position(0, 0, 0)
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

    serial_comm.move('forward')
    try:
        for i, frame in enumerate(camera.capture_continuous(
                rawCapture, format='bgr', use_video_port=True)):
            image = frame.array
            frames.append(image)
            detections, drawn = detector.detect(image)
            r.set('output', serialize.serialize(drawn))
            if len(detections) != 0:
                pass
                # print(len(detections))
            else:
                pass
            rawCapture.truncate(0)
            ticks = serial_comm.read_ticks()
            while ticks is not None:
                dx, dy, dh = rob.update(ticks[0], ticks[1])
                rob.move(dx, dy, dh)
                ticks = serial_comm.read_ticks()
            time.sleep(0.1)
            print(rob.x, rob.y, rob.heading)
            if rob.x > 1000:
                serial_comm.move('stop')
                break
    except Exception as e:
        print(e)
        serial_comm.move('stop')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
