a = int(input('введите число: '))
b = 1
i = 0
for _ in range(a):
    if a % b == 0:
        print(b, end=' ')
        b += 1
        i += 1
    else:
        b += 1
# тут стоит принт так как надо "сбросить" команду end
# если убрать, то будет в одну строчку
print(' ')
if i > 2:
    print('НЕТ')
else:
    print('ДА')
