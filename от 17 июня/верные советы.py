for i in range(int(input())):
    string = str(input())
    if string[0:2] == 'не' or string[0:2] == 'Не':
        print(string[3:])
    else:
        print(string)
# надеюсь не страшно что она сразу выводит проверенную строуку а не все разом в конце работы