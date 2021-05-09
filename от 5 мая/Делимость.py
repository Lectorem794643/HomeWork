i = 0
for _ in range(17):
    a = int(input())
    if i % a == 0:
        print('ДА')
        i += 1
    else:
        print('НЕТ')
        i += 1
