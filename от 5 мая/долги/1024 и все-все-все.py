# проверяет является ли число степенью двойки, и если да, то какой?
# вороде "степень" на наглийском - degree
number = int(input())
degree = 0
x = 0
while number > degree:
    x += 1
    degree = 2 ** x
if number == degree:
    print(x)
else:
    print('error')