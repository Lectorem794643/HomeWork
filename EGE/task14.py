myExpression = 4 * 625 ** 9 - 25 ** 15 + 2 * 5 ** 11 - 7
countOfFours = 0
while myExpression > 0:
    countOfFours += (myExpression % 5 == 4)  # объясни, что здесь происходит
    myExpression //= 5
print(countOfFours)
