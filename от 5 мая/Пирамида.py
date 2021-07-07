height = int(input())  # используй понятные названия переменных
for symbols in range(1, height, 2):  # используй возможности итератора в цикле! вместо _ переменную и считать по ней
    print(' ' * height, '*' * symbols, ' ' * height)
    h -= 1
