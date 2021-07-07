for _ in range(int(input())):
    string = str(input())
    if string[0:2] == 'не' or string[0:2] == 'Не':
        print(string[3:])
    else:
        print(string)
# надеюсь не страшно что она сразу выводит проверенную строуку а не все разом в конце работы
# CORRECT

for _ in range(int(input())):
    badAdvice = str(input())
    if 'не ' in badAdvice[0:3] or 'Не ' in badAdvice[0:3]:
        badAdvice = badAdvice[3:]
    print(badAdvice)