import math
import numpy as np


class Position:
    DIRECTION_LEFT = 0
    DIRECTION_RIGHT = 1

    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading
        self.last_tick_left = None
        self.last_tick_right = None
        self.wheel_radius = 34.6  # mm
        self.wheel_ticks = 40
        self.robot_width = 150  # mm

    def move(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading

    def tick_to_distance(self, ticks):
        return self.wheel_radius * 2 * math.pi * ticks / self.wheel_ticks

    def movement(self, l, r):
        # l and r in mm
        # turning center is P away from center
        # R = (P + w / 2) * theta
        # L = (P - w / 2) * theta
        # theta = (R - L) / w
        # P = (w / 2) * (L + R) / (R - L)
        # ICC = [x - P sin(heading), y + P cos(heading)]
        # rotation_matrix = [
        #   cos(theta), -sin(theta), 0
        #   sin(theta), cos(theta),  0
        #   0         , 0         ,  1
        # ]
        # rotation_matrix * [x - ICCx, y - ICCy, heading] + [ICCx, ICCy, theta]
        theta = (r - l) / self.robot_width
        P = (self.robot_width / 2) * (l + r) / (r - l)
        ICC = [self.x - P * math.sin(self.heading),
               self.y + P * math.cos(self.heading)]
        rot = np.array([
            [math.cos(theta), -math.sin(theta), 0],
            [math.sin(theta), math.cos(theta), 0],
            [0, 0, 1]
        ])
        position = rot @ np.array([self.x - ICC[0],
                                   self.y - ICC[1],
                                   self.heading]).T
        position += np.array([ICC[0], ICC[1], theta]).T
        return position[0] - self.x, position[1] - self.y, position[2] - self.heading

    def update_forward(self, tick_left, tick_right):
        if self.last_tick_left is None:
            self.last_tick_left = tick_left
            self.last_tick_right = tick_right
            return 0
        dticks_left = tick_left - self.last_tick_left
        dticks_right = tick_right - self.last_tick_right
        if dticks_left == dticks_right:
            dist = self.tick_to_distance(dticks_right)
            self.x += math.cos(self.heading) * dist
            self.y += math.sin(self.heading) * dist
            return dist
        r = self.tick_to_distance(dticks_right)
        l = self.tick_to_distance(dticks_left)
        g1, g2, g3 = self.movement(l, r)
        self.x += g1
        self.y += g2
        self.heading += g3
        self.last_tick_left = tick_left
        self.last_tick_right = tick_right
        return math.sqrt(g1 ** 2 + g2 ** 2)

    def update_left(self, tick_left, tick_right):
        if self.last_tick_left is None:
            self.last_tick_left = tick_left
            self.last_tick_right = tick_right
            return 0
        dticks_left = -(tick_left - self.last_tick_left)
        dticks_right = tick_right - self.last_tick_right
        if dticks_left == 0 and dticks_right == 0:
            return 0
        r = self.tick_to_distance(dticks_right)
        l = self.tick_to_distance(dticks_left)
        g1, g2, g3 = self.movement(l, r)
        self.x += g1
        self.y += g2
        self.heading += g3
        self.last_tick_left = tick_left
        self.last_tick_right = tick_right
        return g3

    def update_right(self, tick_left, tick_right):
        if self.last_tick_left is None:
            self.last_tick_left = tick_left
            self.last_tick_right = tick_right
            return 0
        dticks_left = tick_left - self.last_tick_left
        dticks_right = -(tick_right - self.last_tick_right)
        if dticks_left == 0 and dticks_right == 0:
            return 0
        r = self.tick_to_distance(dticks_right)
        l = self.tick_to_distance(dticks_left)
        g1, g2, g3 = self.movement(l, r)
        self.x += g1
        self.y += g2
        self.heading += g3
        self.last_tick_left = tick_left
        self.last_tick_right = tick_right
        return g3
