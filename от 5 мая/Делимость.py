i = 0
for _ in range(17):
    a = int(input())
    if i % a == 0:
        print('ДА')
        i += 1
    else:
        print('НЕТ')
        i += 1
# ты использовал счетчик вместо того, чтобы использовать возможности цикла
for number in range(0, 17):
    modular = int(input())
    if number % modular == 0:
        print('ДА')
    else:
        print('НЕТ')
