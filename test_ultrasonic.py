import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 5  # 23
ECHO = 6  # 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

time.sleep(2)

for i in range(100):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    print('Distance', distance, 'cm')
    time.sleep(0.1)

GPIO.cleanup()


