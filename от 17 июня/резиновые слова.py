word = str(input())
if len(word) % 2 == 0:
    print(' ' * int((len(word)) / 2 - 1), word[int(len(word) / 2) - 1:int(len(word) / 2) + 1])
    counter = distance = int((len(word)) / 2 - 2)
    counter_R = counter + 3
    while counter >= 0:
        print(' ' * (counter), word[counter], ((distance - counter) * 2) * ' ', word[counter_R])
        counter -= 1
        counter_R += 1
if len(word) % 2 != 0:



#  синхрофазатрон
