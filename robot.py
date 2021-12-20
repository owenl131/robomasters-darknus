import math


class Position:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading
        self.last_tick_left = 0
        self.last_tick_right = 0
        self.wheel_radius = 30  # mm
        self.wheel_ticks = 40
        self.robot_width = 100  # mm

    def tick_to_distance(self, ticks):
        return self.wheel_radius * 2 * math.pi * ticks / self.wheel_ticks

    def update(self, tick_left, tick_right):
        dticks_left = tick_left - self.last_tick_left
        dticks_right = tick_right - self.last_tick_right
        if dticks_left == dticks_right:
            dist = self.tick_to_distance(dticks_right)
            g1 = math.cos(self.heading) * dist
            g2 = math.sin(self.heading) * dist
            g3 = 0
        else:
            alpha = (dticks_right - dticks_left) / self.robot_width
            rad = dticks_left / alpha
            g1 = self.x + (rad + self.robot_width/2) * \
                (math.sin(self.heading+alpha) - math.sin(self.heading))
            g2 = self.y + (rad + self.robot_width/2) * \
                (-math.cos(self.heading+alpha) + math.cos(self.heading))
            g3 = (self.heading + alpha + math.pi) % (2*math.pi) - math.pi
        self.last_tick_left = tick_left
        self.last_tick_right = tick_right
        return g1, g2, g3
