stringOfDecimals = '1' * 81
while '1111' in stringOfDecimals or '88888' in stringOfDecimals:
    if '1111' in stringOfDecimals:
        stringOfDecimals = stringOfDecimals.replace('1111', '888', 1)
    else:
        stringOfDecimals = stringOfDecimals.replace('88888', '888', 1)
print(stringOfDecimals)