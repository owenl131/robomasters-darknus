import serial
import os
import time


acm = [x for x in os.listdir('/dev') if x.startswith('ttyACM')][0]
print(acm)
ser = serial.Serial('/dev/' + acm, 38400, timeout=1, write_timeout=1)
ser.flush()

CODE_FORWARD = b'bm'
CODE_BACKWARD = b'cm'
CODE_LEFT = b'dm'
CODE_RIGHT = b'em'
CODE_STOP = b'sm'

buffer_read = ''


def read_ticks():
    global buffer_read
    if ser.in_waiting > 0:
        buffer_read += ser.read(ser.in_waiting).decode('utf-8')
    # print(buffer_read)
    if '\n' in buffer_read:
        index = buffer_read.index('\n')
        data = buffer_read[:index]
        buffer_read = buffer_read[index + 1:]
        try:
            values = list(map(int, data.split(',')))
            if len(values) == 2:
                return values
        except:
            pass
    return None


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


if __name__ == '__main__':
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    print(ser.write(CODE_FORWARD))
    time.sleep(3)
    print(ser.write(CODE_STOP))

