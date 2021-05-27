print('Инструкция: калькулятор - запущен, для остановки введите "STOP"')
STOP = True
while STOP:
    error_flag = True
    sign = input("Какую операцию необходимо провести (+,-,/,*, Factorial, %) :")
    if sign != '+' and sign != '-' and sign != '/' and sign != '*' and sign != 'Factorial' and sign != '%':
        print('НЕДОПУСТИМАЯ ОПЕРАЦИЯ')
        print('ERROR')
        error_flag = False
    if error_flag:
        a = int(input('Введите первое число :'))
        if sign == 'Factorial':
            factorial = 1
            for i in range(1, a + 1):
                factorial *= i
            print('Факториал =', factorial)
        else:
            b = int(input("Введите второе число :"))
            if sign == '+':
                c = a + b
                print('ответ =', c)
            elif sign == '-':
                c = a - b
                print(c)
            elif sign == '/':
                if b != 0:
                    c = a // b
                    print('ответ =', c)
                else:
                    print('На 0 делить нальзя!')
            elif sign == '*':
                c = a * b
                print('ответ =', c)
            elif sign == '%':
                print('ответ =', a % b)
            elif sign == 'STOP':
                STOP = False
            print('Операция завершена!')
    else:
        print('Операция превана, RESTART')
print('Работа окончена, спасибо!')
