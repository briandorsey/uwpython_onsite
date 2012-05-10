"""
Vehicles for traffic simulation
From Jon Jacky's Intro to Python course:
    http://staff.washington.edu/jon/python-course/
"""


class Vehicle(object):
    """
    Vehicle base class for traffic simulation
    """
    census = 0  # number of Vehicles created

    def __init__(self, position=0, velocity=0, icon='V'):
        self.x = position  # Just one dimension for now
        self.v = velocity  # negative v moves toward smaller x (left)
        self.icon = '%s%s' % (icon, Vehicle.census)  # ID string
        Vehicle.census += 1

    def __str__(self):
        return '%s: x %s, v %s' % (self.icon, self.x, self.v)

    def move(self, dt=1, signals=None):
        """
        move self for time interval dt, update position
        possibly respond to signals from the environment
        """
        self.x += dt * self.v
        

    def draw(self, view):
        """
        draw self at position in view
        """
        l = len(self.icon)
        if 0 < self.x < (len(view) - l):
            view[self.x:self.x + l] = self.icon


class SafeVehicle(Vehicle):
    """
    Safe Vehicle subclass of Vehicle base class, change move behavior
    """
    def __init__(self, position=0, velocity=0, icon='S'):
        Vehicle.__init__(self, position, velocity, icon)

    def move(self, dt=1, signals=None):
        """
        Do not move when 'R' (red light) in signals
        """
        if 'R' not in signals:
            self.x += dt * self.v


if __name__ == '__main__':
    v0 = Vehicle()
    v1 = Vehicle(10)
    v2 = Vehicle(30, -20)
    v3 = SafeVehicle(20, 5)
    print v0
    print v1
    print v2
    print v3
    v0.move()
    v1.move()
    stoplight = ('R',)  # red light
    v2.move(signals=stoplight)  # ignore
    v3.move(signals=stoplight)  # obey
    print 'After move:'
    print v0
    print v1
    print 'After move with red stoplight:'
    print v2
    print v3
