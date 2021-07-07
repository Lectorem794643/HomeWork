quantityOfNumbers, maxNumber = 0, 0
for number in range(12972, 89323):
    if number % 13 == 7 and number % 7 != 0 and number % 11 != 0:
        quantityOfNumbers, maxNumber = quantityOfNumbers + 1, number
print(quantityOfNumbers, maxNumber)
