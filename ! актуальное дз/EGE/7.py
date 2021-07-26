P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for A in range(-100000, 100000):
    for X in range(-100000, 100000):
        if all(((not (X in P)) in (X in A)) or ((X in A) in (not (X in Q)))):
            print(A)
