# oч странная программа, не уверен что она работает правильно,
# но похоже вроде

q = int(input('количество людей = '))  # аргумент input мы еще не проходили, но ок, почему нет нормальных наименований?
sumIQ = 0
L = 0
for _ in range(q):
    IQ = int(input('IQ человека = '))
    L += 1  # та же ошибка, что и везде раньше, не используешь возможности итератора
    if ( sumIQ / L ) > IQ:  # лишние пробелы
        print('ниже среднего', sumIQ / L)
    elif ( sumIQ / L ) < IQ:
        print('выше среднего', sumIQ / L)
    elif ( sumIQ / L ) == IQ:
        print('равен среднему', sumIQ / L)
    else:
        print('0')
    sumIQ += IQ  # почему стоит использовать в начале цикла?

# эталонное решение:

n = int(input())
total = 0
for i in range(1, n + 1):
    number = int(input())
    sum += number
    if number == total / i:
        print('0')
    elif number < total / i:
        print('<')
    elif number > total / i:
        print('>')
