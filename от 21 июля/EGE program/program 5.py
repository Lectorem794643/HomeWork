stringOfDecimals = '1' * 46 + '2' * 46
while '111' in stringOfDecimals:
    if '111' in stringOfDecimals:
        stringOfDecimals = stringOfDecimals.replace('111', '2', 1)
    if '222' in stringOfDecimals:
        stringOfDecimals = stringOfDecimals.replace('222', '1', 1)
print(stringOfDecimals)