# пользователь вводит ряд чисел и просят
# сложить или вычисть число в зависмости от того, четный номер или нет

rowLength = int(input())
Sum = 0
for i in range(1, rowLength + 1):
    number = int(input())
    if i % 2 == 0:
        Sum -= number
    else:
        Sum += number
print(Sum)