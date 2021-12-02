import serial
import time
import keyboard

ser = serial.Serial('/dev/ttyACM0', 38400, timeout=1)
ser.flush()

CODE_FORWARD = b'a'
CODE_BACKWARD = b'b'
CODE_LEFT = b'c'
CODE_RIGHT = b'd'
CODE_STOP = b's'

keyboard.on_press_key('left', lambda: ser.write(CODE_LEFT))
keyboard.on_press_key('right', lambda: ser.write(CODE_RIGHT))
keyboard.on_press_key('up', lambda: ser.write(CODE_FORWARD))
keyboard.on_press_key('down', lambda: ser.write(CODE_BACKWARD))
keyboard.on_release_key('left', lambda: ser.write(CODE_STOP))
keyboard.on_release_key('right', lambda: ser.write(CODE_STOP))
keyboard.on_release_key('up', lambda: ser.write(CODE_STOP))
keyboard.on_release_key('down', lambda: ser.write(CODE_STOP))

