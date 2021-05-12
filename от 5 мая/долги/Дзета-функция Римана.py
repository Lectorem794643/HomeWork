# программа которая считает что-то по заданой формуле и введеному
# значению. работает вроде корректно.

number = int(input())
SUMinverseSquare = 0
for i in range(1, number + 1):
    inverseSquare = 1 / i ** 2
    SUMinverseSquare += inverseSquare
print((3.1415926535 ** 2) / SUMinverseSquare)
