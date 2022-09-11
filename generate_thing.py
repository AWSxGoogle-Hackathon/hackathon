import time
import math
import random
random.seed(0)

phase = 0

things = [10 * (2 + math.sin(phase/3)) + (1 + math.sin(phase/30)) + abs(random.normalvariate(0, 10)) for phase in range(100)]

with open('db.txt', 'a') as f:
    for k in range(100):
        f.write('else if (lol[0].y === ' + str(things[-1]) +  ') { lol = [')
        for i in range(36):
            f.write('{x: ' + str(i) + ', y: ' + str(things[i]) + '}, ')
        f.write(']}\n')
        back = things[0]
        things.pop(0)
        things.append(back)