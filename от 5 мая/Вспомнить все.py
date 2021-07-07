# Все верно, но используем temperature вместо t
temperature = float(input('Введите температуру :'))
if temperature < 15.5:
    print('Холодно')
elif temperature > 28:
    print('Жарко')
else:
    print('Нормально')
