with open('24.txt', 'r') as file:
    data = file.read()
lengthCounter = 1
maxLength = 0
for i in range(len(data)):
    if lengthCounter % 2 == 1 and data[i] == 'A':
        lengthCounter += 1
        maxLength = max(maxLength, lengthCounter)
    elif lengthCounter % 2 == 0 and (data[i] == 'B' or data[i] == 'C'):
        lengthCounter += 1
        maxLength = max(maxLength, lengthCounter)
    else:
        lengthCounter = 1
print((maxLength - 1) // 2)
