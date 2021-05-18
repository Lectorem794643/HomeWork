print('Инструкция - калькулятор запущен, для остановки введите "STOP"')
STOP = True
while STOP:
    sign = input("Какую операцию необходимо провести (+,-,/,*) :")
    a = float(input('Введите первое число :'))
    b = float(input("Введите второе число :"))
    if sign == '+':
        c = a + b
        print(c)
    elif sign == '-':
        c = a - b
        print(c)
    elif sign == '/':
        if b != 0:
            c = a / b
            print(c)
        else:
            print('На 0 делить нальзя!')
    elif sign == '*':
        c = a * b
        print(c)
    elif sign == 'STOP':
        STOP = False
    else:
        print('ERROR')
        STOP = False
    print('Операция завершена!')
print('Работа окончена, спасибо!')