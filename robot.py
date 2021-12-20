import math


class Position:
    DIRECTION_LEFT = 0
    DIRECTION_RIGHT = 1

    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading
        self.last_tick_left = None
        self.last_tick_right = None
        self.wheel_radius = 32  # mm
        self.wheel_ticks = 40
        self.robot_width = 150  # mm


    def move(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading


    def tick_to_distance(self, ticks):
        return self.wheel_radius * 2 * math.pi * ticks / self.wheel_ticks


    def update_rotate(self, tick_left, tick_right, direction):
        dticks_left = tick_left - self.last_tick_left
        dticks_right = tick_right - self.last_tick_right
        if dticks_left == 0 and dticks_right == 0:
            return self.x, self.y, self.heading
        r = self.tick_to_distance(dticks_right)
        l = self.tick_to_distance(dticks_left)
        alpha = (r + l) / self.robot_width * (1 if direction == Position.DIRECTION_LEFT else -1)
        rad = (r - l) / (2 * alpha)
        g1 = self.x - rad * math.cos(self.heading) + rad * math.cos(self.heading + alpha)
        g2 = self.y - rad * math.sin(self.heading) + rad * math.sin(self.heading + alpha)
        g3 = (self.heading + alpha + math.pi) % (2 * math.pi) - math.pi
        return g1, g2, g3


    def update_forward(self, tick_left, tick_right):
        if self.last_tick_left is None:
            self.last_tick_left = tick_left
            self.last_tick_right = tick_right
            return self.x, self.y, self.heading
        dticks_left = tick_left - self.last_tick_left
        dticks_right = tick_right - self.last_tick_right
        if dticks_left == dticks_right:
            dist = self.tick_to_distance(dticks_right)
            g1 = self.x + math.cos(self.heading) * dist
            g2 = self.y + math.sin(self.heading) * dist
            g3 = self.heading
        else:
            r = self.tick_to_distance(dticks_right)
            l = self.tick_to_distance(dticks_left)
            alpha = (l - r) / self.robot_width
            rad = l / alpha
            g1 = self.x + (rad + self.robot_width/2) * \
                (math.sin(self.heading+alpha) - math.sin(self.heading))
            g2 = self.y + (rad + self.robot_width/2) * \
                (-math.cos(self.heading+alpha) + math.cos(self.heading))
            g3 = (self.heading + alpha + math.pi) % (2*math.pi) - math.pi
        self.last_tick_left = tick_left
        self.last_tick_right = tick_right
        return g1, g2, g3
