from itertools import *  # импортируем из библиотеки itertools все команды
for a, b, c, d in product([0, 1], repeat=4):
    if not((not a and not b) or (b == c) or d):
        print(a, b, c, d)

# Читай https://python-scripts.com/itertools :: product и repeat
