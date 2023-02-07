from draw2d import *
from vectors import add, scale
t = 0
s = (0, 0)
v = (1, 0)
a = (0, 0.2)

dt = 2
steps = 5


positions = [s]

for _ in range(0, 5):
    t += 2
    s = add(s, scale(dt, v))

    v = add(v, scale(dt, a))
    positions.append(s)

print(positions)
draw2d(Points2D(*positions))
