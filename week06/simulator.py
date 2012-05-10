"""
Traffic simulation
From Jon Jacky's Intro to Python course:
    http://staff.washington.edu/jon/python-course/
"""

from vehicle import Vehicle, SafeVehicle
from pedestrian import Pedestrian
from random import randint

WIDTH = 65  # portion of one-dimensional space included in view

VEHICLE_COUNT = 2
SAFE_VEHICLE_COUNT = 1
PEDESTRIAN_COUNT = 1

vehicles = []
for i in range(VEHICLE_COUNT):
    vehicles.append(Vehicle(randint(1, WIDTH - 1),
                            randint(-4, 4)))

for i in range(SAFE_VEHICLE_COUNT):
    vehicles.append(SafeVehicle(randint(1, WIDTH - 1),
                                randint(-4, 4)))

for v in vehicles:
    print v, '   ',
print


def clear(view):
    for i in range(WIDTH):
        view[i] = '.'


nsteps = 10
stoplight = 'G'  # green, go
view = list('.' * WIDTH)
for t in range(nsteps):
    clear(view)
    if t == 6:
        stoplight = 'R'  # red, stop
        for i in range(PEDESTRIAN_COUNT):
            vehicles.append(Pedestrian(randint(1, WIDTH - 1)))
    for v in vehicles:
        v.move(signals=stoplight)
        v.draw(view)
    print ''.join(view), stoplight  # generate string from view
