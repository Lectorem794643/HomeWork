# win = False
# left = 0
# right = 1001
# while not win:
#     number = (left + right) // 2
#     print(number)
#     sign = input()
#     if sign == '<':
#         right = number
#     elif sign == '>':
#         left = number
#     else:
#         print('я угадал, это число -', number)
#         win = True
#
# # CORRECT
# # Неплохо, но есть ряд вопросов: 1. Зачем left 2. Почему right = 1001, а не 1000
# # 3. Есть ли алгоритм поиска более оптимальный
# # Ниже пример оптимизированого алгоритма, проанализируй его:

firstStep = False
answer = ""
limit = 1000
print("Загадай число от 1 до 1000")
print("Это число ", limit // 2, "?")
while answer != "=":
    if firstStep:
        print("Это число ", limit, "?")
    answer = str(input())
    print(limit)
    if answer == ">":
        limit = round(limit * 0.75, 1)
        print(limit)
    elif answer == "<":
        limit = round(limit * 0.25, 1)
    else:
        print("УРА!!")
    firstStep = True
