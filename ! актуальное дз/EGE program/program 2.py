from itertools import *
for x, y, z in product([0, 1], repeat=3):
    if (not x and y) or (y and z):
        print(x, y, z)
# прям решение получилось, отлично
