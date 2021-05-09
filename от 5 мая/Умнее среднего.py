# oч странная программа, не уверен что она работает правильно,
# но похоже вроде

q = int(input('количество людей = '))
sumIQ = 0
L = 0
for _ in range(q):
    IQ = int(input('IQ человека = '))
    L += 1
    if ( sumIQ / L ) > IQ:
        print('ниже среднего', sumIQ / L)
    elif ( sumIQ / L ) < IQ:
        print('выше среднего', sumIQ / L)
    elif ( sumIQ / L ) == IQ:
        print('равен среднему', sumIQ / L)
    else:
        print('0')
    sumIQ += IQ
