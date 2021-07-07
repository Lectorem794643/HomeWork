repeat = int(input())
for i in range(repeat):
    answer = 0
    error = True
    while error:
        one = input()
        if one == 'раз':
            answer += 1
            two = input()
            if two == 'два':
                answer += 1
                three = input()
                if three == 'три':
                    answer += 1
                    four = input()
                    if four == 'четыре':
                        answer += 1
        else:
            error = False
    ans = str(answer)
    print('Правильных отсчётов было', answer, ', но теперь вы ошиблись.')
print('На сегодня хватит.')

# WRONG
# Тестируй на примерах
