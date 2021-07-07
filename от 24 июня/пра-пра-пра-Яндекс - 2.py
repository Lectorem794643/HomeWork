printString = True
dataQuery, searchQuery = [], []
for _ in range(int(input())):
    dataQuery.append(str(input()))
for _ in range(int(input())):
    searchQuery.append(str(input()))
for result in dataQuery:
    for symbol in searchQuery:
        if symbol not in result:
            printString = False
            break
    if printString:
        print(result)
    printString = True
