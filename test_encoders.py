import RPi.GPIO as GPIO
import time

try:
    GPIO.setmode(GPIO.BCM)
    INPUT = 18
    INPUT_A = 23
    GPIO.setup(INPUT, GPIO.IN)
    GPIO.setup(INPUT_A, GPIO.IN)
    for i in range(100):
        print(GPIO.input(INPUT))
        print(GPIO.input(INPUT_A))
        time.sleep(0.1)

except:
    pass
finally:
    GPIO.cleanup()


