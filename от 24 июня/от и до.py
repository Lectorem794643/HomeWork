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
low, high = int(input()), int(input())
summa = 0
for i in (database[low - 1:high]):
    summa += i
print(summa)