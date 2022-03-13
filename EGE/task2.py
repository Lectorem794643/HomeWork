from itertools import *
for w, x, y, z in product([0, 1], repeat=4):
    if not((w == z) or (x and (not y)) or w):
        print(w, x, y, z)
