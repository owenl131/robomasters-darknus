
class Point:
    def __init__(x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(p1, p2):
        self.p1 = p1
        self.p2 = p2

arena = [
    Line(Point(0, 0), Point(0, 6)),
    Line(Point(0, 6), Point(6, 6)),
    Line(Point(6, 6), Point(6, 0)),
    Line(Point(6, 0), Point(0, 0)),
    
]



