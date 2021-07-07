stringOfDecimals = '1' * 100
while '111' in stringOfDecimals or '88888' in stringOfDecimals:
    if '111' in stringOfDecimals:
        stringOfDecimals = stringOfDecimals.replace('111', '88', 1)
    else:
        stringOfDecimals = stringOfDecimals.replace('88888', '8', 1)
print(stringOfDecimals)

# Скоро дойдем до методов обработки строк, познакомишься и с replace
