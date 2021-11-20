myString = '1110101001010100'
zippedCode = ''
symbolsCounter = 1
for i in range(len(myString) - 1):
    if i == (len(myString) - 2) and (myString[i] == myString[i + 1]):
        symbolsCounter += 1
        if myString[i] == '0':
            zippedCode += 'Z' + str(symbolsCounter)
        else:
            zippedCode += 'X' + str(symbolsCounter)
        break
    else:
        if myString[i] == '0' and myString[i + 1] != '0':
            zippedCode += 'Z' + str(symbolsCounter)
            symbolsCounter = 1
        elif myString[i] == '1' and myString[i + 1] != '1':
            zippedCode += 'X' + str(symbolsCounter)
            symbolsCounter = 1
        else:
            symbolsCounter += 1
print(zippedCode)
