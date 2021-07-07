i = 0
while i != 1:
    a = str(input())
    if len(a) != 0:
        print(a)
    else:
        i += 1
print('end')

# все то же, что и раньше + избыточное решение по end, пример:
myString = str(input())
while len(myString) != 0:
    print(myString)
    myString = str(input())
