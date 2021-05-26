n = int(input())
cat_flag = False
for i in range(n):
    phrase = input()
    if 'Кот' in phrase or 'кот' in phrase:
        flagcat = True
        # посмотрел есть ли там кот
    elif 'Пёс' in phrase or 'пёс' in phrase:
        cat_flag = False
        # если есть кот, проверил на отсутствие пса
if cat_flag is True:
    print('meow')
elif cat_flag is False:
    print('The cat is lost')
