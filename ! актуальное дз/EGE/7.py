P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
numbersA = 0
for x in range(100):
    if (x in P) and (x in Q):
        numbersA += 1
print(numbersA)