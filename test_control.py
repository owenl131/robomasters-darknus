import serial
import time

ser = serial.Serial('/dev/ttyACM0', 38400, timeout=1)
ser.flush()

CODE_FORWARD = b'b'
CODE_BACKWARD = b'c'
CODE_LEFT = b'd'
CODE_RIGHT = b'e'
CODE_STOP = b's'
CODE_MEDIUM = b'm'
run = True


while run:
    k = input()
    if k == 'q':
        break
    if k == 'a':
        ser.write(CODE_LEFT)
        ser.write(CODE_MEDIUM)
    if k == 'd':
        ser.write(CODE_RIGHT)
        ser.write(CODE_MEDIUM)
    if k == 'w':
        ser.write(CODE_FORWARD)
        ser.write(CODE_MEDIUM)
    if k == 's':
        ser.write(CODE_BACKWARD)
        ser.write(CODE_MEDIUM)
    if k == '':
        ser.write(CODE_STOP)
        ser.write(CODE_MEDIUM)

