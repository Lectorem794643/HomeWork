win = False
left = 0
right = 1001
while not win:
    number = (left + right) // 2
    print(number)
    sign = input()
    if sign == '<':
        right = number
    elif sign == '>':
        left = number
    else:
        print('я угадал, это число -', number)
        win = True
