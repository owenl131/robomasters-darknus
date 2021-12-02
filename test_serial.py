import serial
import time

ser = serial.Serial('/dev/ttyACM0', 38400, timeout=1)
ser.flush()

ser.write(b'b')
time.sleep(2)
ser.write(b's')
time.sleep(2)
ser.write(b'c')
time.sleep(2)
ser.write(b's')
time.sleep(2)
ser.write(b'd')
time.sleep(2)
ser.write(b's')

