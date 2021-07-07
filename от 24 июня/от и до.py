database = []
for _ in range(int(input())):
    database += [int(input())]
low, high = int(input()), int(input())
c = 0
print(database)
for i in range(low - 1, high):
    c += database[i]
print(c)

database = []
for _ in range(int(input())):
    database += [int(input())]
rangeMin, rangeMax = int(input()), int(input())
rangeSum = 0
for number in (database[rangeMin - 1:rangeMax]):
    rangeSum += number
print(rangeSum)