Решение задачи последовательным перебором

with open('24.txt', 'r') as file:
    bigString = str(file.read())
maxLength, currentLength, tooMuchD = 0, 0, False

for letter in bigString:
    if letter != 'D':
        currentLength += 1
    elif letter == 'D' and not tooMuchD:
        currentLength += 1
        tooMuchD = not tooMuchD
    else:
        maxLength = max(maxLength, currentLength)
        currentLength = 0
        tooMuchD = not tooMuchD

currentLength, tooMuchD = 0, False
for letter in bigString[bigString.index('D') + 1:]:
    if letter != 'D':
        currentLength += 1
    elif letter == 'D' and not tooMuchD:
        currentLength += 1
        tooMuchD = not tooMuchD
    else:
        maxLength = max(maxLength, currentLength)
        currentLength = 0
        tooMuchD = not tooMuchD

print(maxLength)

Решение задачи нарезкой на отрезки

with open('24.txt', 'r') as file:
    betweenDSequences = [len(x) for x in file.read().split('D')]
doubledSequences = []
for i in range(len(betweenDSequences) - 1):
    doubledSequences.append(betweenDSequences[i] + 1 + betweenDSequences[i + 1])
print(max(doubledSequences))