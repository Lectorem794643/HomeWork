database = []
for _ in range(int(input())):
    database += [int(input())]
for i in range(len(database)):
    print(database[i] + database[i + 1])
# при работе выдает ошибку, но работает правильно
