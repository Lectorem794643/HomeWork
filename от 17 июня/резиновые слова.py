word = str(input())
if len(word) % 2 == 0:
    print(' ' * int((len(word)) / 2 - 1), word[int(len(word) / 2) - 1:int(len(word) / 2) + 1])
    counter = distance = int((len(word)) / 2 - 2)
    counter_R = counter + 3
    while counter >= 0:
        print(' ' * (counter), word[counter], ((distance - counter) * 2) * ' ', word[counter_R])
        counter -= 1
        counter_R += 1
elif len(word) % 2 != 0:
    print(' ' * (len(word) // 2 + 1), word[len(word) // 2])
    counter = len(word) // 2
    distance = 1
    counter_R = len(word) - len(word) // 2
    while counter > 0:
        print(' ' * (counter - 1), word[counter - 1], ' ' * distance, word[counter_R])
        distance += 2
        counter -= 1
        counter_R += 1
else:
    print('Error (мы работаем над этим)')


# синхрофазатрон
# рогатка
