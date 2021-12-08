import serial

ser = serial.Serial('/dev/ttyACM0', 38400, timeout=1)
ser.flush()

CODE_FORWARD = b'b'
CODE_BACKWARD = b'c'
CODE_LEFT = b'd'
CODE_RIGHT = b'e'
CODE_STOP = b's'

def move(direction):
    if direction == 'left':
        ser.write(CODE_LEFT)
    elif direction == 'right':
        ser.write(CODE_RIGHT)
    elif direction == 'forward':
        ser.write(CODE_FORWARD)
    elif direction == 'backward':
        ser.write(CODE_BACKWARD)
    else:
        ser.write(CODE_STOP)


