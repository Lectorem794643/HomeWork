# мне не нравится вывод этой программы
for i in range(int(input())):
    string = str(input())
    if string[:4] == '####':
        print()
    if string[:2] == '%%':
        print(string[2:])
    else:
        print(string)

# вот тут вывод лучше, но она сама более громоздкая
for i in range(int(input())):
    string = str(input())
    flag = True
    if string[:2] == '%%':
        print(string[2:])
        flag = False
    if string[:4] == '####':
        print()
        flag = False
    if flag:
        print(string)