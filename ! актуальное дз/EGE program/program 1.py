from itertools import *
for x, y, z, w in product([0, 1], repeat=4):
    if (((not y) or w) == (not x or (not z))) and (x or w):
        print(x, y, z, w)
# помогает конечно

