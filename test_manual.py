import serial
import time
# import keyboard

ser = serial.Serial('/dev/ttyACM0', 38400, timeout=1)
ser.flush()

CODE_FORWARD = b'b'
CODE_BACKWARD = b'c'
CODE_LEFT = b'd'
CODE_RIGHT = b'e'
CODE_STOP = b's'

run = True

'''keyboard.on_press_key('a', lambda: ser.write(CODE_LEFT))
keyboard.on_press_key('right', lambda: ser.write(CODE_RIGHT))
keyboard.on_press_key('up', lambda: ser.write(CODE_FORWARD))
keyboard.on_press_key('down', lambda: ser.write(CODE_BACKWARD))
keyboard.on_release_key('a', lambda: ser.write(CODE_STOP))
keyboard.on_release_key('right', lambda: ser.write(CODE_STOP))
keyboard.on_release_key('up', lambda: ser.write(CODE_STOP))
keyboard.on_release_key('down', lambda: ser.write(CODE_STOP))

def on_press(key):
    print(key)
    global run
    if key == 'a':
        ser.write(CODE_LEFT)
    if key == 'q':
        run = False

def on_release(key):
    ser.write(CODE_STOP)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

keyboard.on_press(on_press)
keyboard.on_release(on_release)'''

while run:
    k = input()
    if k == 'q':
        break
    if k == 'a':
        ser.write(CODE_LEFT)
    if k == 'd':
        ser.write(CODE_RIGHT)
    if k == 'w':
        ser.write(CODE_FORWARD)
    if k == 's':
        ser.write(CODE_BACKWARD)
    if k == '':
        ser.write(CODE_STOP)

