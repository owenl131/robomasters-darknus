import time
import serial_comm
import redis
import robot
import math


def forward(rob, distance):
    serial_comm.move('forward')
    while True:
        ticks = serial_comm.read_ticks()
        while ticks is not None:
            travelled = rob.update_forward(ticks[0], ticks[1])
            distance -= travelled
            ticks = serial_comm.read_ticks()
        if distance < 0:
            break
        time.sleep(0.03)
    serial_comm.move('stop')


def turn(rob, angle):
    direction = 'right' if angle < 0 else 'left'
    angle = abs(angle)
    serial_comm.move(direction)
    while True:
        ticks = serial_comm.read_ticks()
        while ticks is not None:
            if direction == 'left':
                travelled = rob.update_left(ticks[0], ticks[1])
            if direction == 'right':
                travelled = rob.update_right(ticks[0], ticks[1])
            travelled = abs(travelled)
            angle -= travelled
            ticks = serial_comm.read_ticks()
        if angle < 0:
            break
        time.sleep(0.03)
    serial_comm.move('stop')


def main():
    rob = robot.Position(0, 0, math.pi / 2)
    r = redis.Redis()
    forward(rob, 1000)
    turn(rob, -math.pi / 2)
    forward(rob, 500)
    turn(rob, math.pi)
    forward(rob, 500)
    turn(rob, math.pi / 2)
    forward(rob, 1000)
    turn(rob, -math.pi)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
