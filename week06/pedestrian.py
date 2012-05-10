"""
Pedestrian for traffic simulation
From Jon Jacky's Intro to Python course:
    http://staff.washington.edu/jon/python-course/
"""


class pedestrian(object):
    """
    Not a subclass of vehicle, but has the same methods
    """
    def __init__(self, position=0):
        self.pos = position

    def __str__(self):
        return 'P: pos %s' % self.pos

    def move(self, dt=1, signals=1):
        self.pos += 1

    def draw(self, view):
        if 0 <= self.pos < len(view):
            view[self.pos] = 'P'

if __name__ == '__main__':
    p0 = pedestrian(10)
    print p0
