string = str(input())
counter = len(string)
q = 0
while counter >= 0:
    print(string[q:-q])
    q += 1
    counter -= 2
# тут что-то сломано, но я не могу понять что(((


wordToEat = str(input())
while len(wordToEat) > 0:
    print(wordToEat)
    wordToEat = wordToEat[0:len(wordToEat) - 1]
    wordToEat = wordToEat[1:len(wordToEat)]