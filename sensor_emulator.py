import time
import math
import random
random.seed(0)

phase = 0

def add_entry(entry):
    with open('db.txt', 'a') as f:
        f.write(str(entry) + '\n')

while True:
    add_entry(10 * (2 + math.sin(phase/3)) + (1 + math.sin(phase/30)) + abs(random.normalvariate(0, 10)))
    phase += 1
    time.sleep(0.1)