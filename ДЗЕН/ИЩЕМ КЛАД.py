x, y, n = 0, 0, 0
flag_WIN = True
new_x, new_y, instruction, steps = int(input()), int(input()), input(), int(input())
while instruction != 'стоп':
    if new_x == x and new_y == y:
        flag_WIN = False
    if instruction == 'север':
        y += steps
        if flag_WIN:
            n += 1
    elif instruction == 'запад':
        x -= steps
        if flag_WIN:
            n += 1
    elif instruction == 'юг':
        y -= steps
        if flag_WIN:
            n += 1
    elif instruction == 'восток':
        x += steps
        if flag_WIN:
            n += 1
    instruction = input()
    if instruction != 'стоп':
        steps = int(input())
print(n)
