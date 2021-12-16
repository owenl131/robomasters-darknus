import serial
import time

ser = serial.Serial('/dev/ttyACM1', 38400, timeout=1)
ser.flush()

ser.write(b'bl')
time.sleep(2)
ser.write(b'ss')
time.sleep(2)
ser.write(b'cl')
time.sleep(2)
ser.write(b'ss')
time.sleep(2)
ser.write(b'dl')
time.sleep(2)
ser.write(b'ss')

