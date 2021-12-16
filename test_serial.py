import serial
import time
import serial_comm

serial_comm.move('forward')
# ser.write(b'bl')
print(serial_comm.read_ticks())
time.sleep(2)
serial_comm.move('stop')
print(serial_comm.read_ticks())
time.sleep(2)
serial_comm.move('backward')
print(serial_comm.read_ticks())
time.sleep(2)
serial_comm.move('stop')
print(serial_comm.read_ticks())
time.sleep(2)
serial_comm.move('right')
print(serial_comm.read_ticks())
time.sleep(2)
serial_comm.move('stop')
print(serial_comm.read_ticks())
