from itertools import *
for x, y, z in product([0, 1], repeat=3):
    if ((not z) and x) or (x and y):
        print(x, y, z)