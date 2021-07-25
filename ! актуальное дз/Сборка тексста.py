positions = [int(i) for i in input().split()]
words = [str(i.lower()) for i in input().split()]
for i in range(len(positions)):
    if i == 0:
        print(words[positions[i] - 1].capitalize(), end=' ')
    else:
        print(words[positions[i] - 1], end=' ')
# Буря мглою небо ĸроет
