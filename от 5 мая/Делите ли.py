a = int(input('введите число: '))
b = 1
i = 0
# используй понятные именования переменных!
for _ in range(a):
    if a % b == 0:
        print(b, end=' ')
        b += 1  # ты не используешь возможности цикла по итерации и вместо них вводишь дополнительные счетчики
        i += 1
    else:
        b += 1
# тут стоит принт так как надо "сбросить" команду end
# если убрать, то будет в одну строчку
# вместо этого можно было бы использовать print('\nНЕТ')
if i > 2 :  # а если равен 1?
    print('\nНЕТ')
else:
    print('\nДА')
