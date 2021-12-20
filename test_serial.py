import serial
import time
import serial_comm

print(serial_comm.read_ticks())
serial_comm.move('forward')
time.sleep(2)
print(serial_comm.read_ticks())
serial_comm.move('stop')
time.sleep(2)
print(serial_comm.read_ticks())
serial_comm.move('backward')
time.sleep(2)
print(serial_comm.read_ticks())
serial_comm.move('stop')
time.sleep(2)
print(serial_comm.read_ticks())
serial_comm.move('right')
time.sleep(2)
print(serial_comm.read_ticks())
serial_comm.move('stop')
