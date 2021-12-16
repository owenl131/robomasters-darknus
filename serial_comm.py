import serial
import struct

ser = serial.Serial('/dev/ttyACM1', 38400, timeout=1)
ser.flush()

CODE_FORWARD = b'bl'
CODE_BACKWARD = b'cl'
CODE_LEFT = b'dl'
CODE_RIGHT = b'el'
CODE_STOP = b'sl'


def read_ticks():
    result = None
    while ser.in_waiting:
        data = ser.read(size=16)
        result = struct.unpack('II', data)
    return result


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
