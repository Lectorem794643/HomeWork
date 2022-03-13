fiveNumbersCounter = 0
for number in range(1200000, 1, -1):
    tripleDivisor, sumOfTripleDivisors = 0, 0
    for divisors in range(2, int(number ** 0.5) + 1):
        if number % divisors == 0:
            sumOfTripleDivisors += number // divisors
            tripleDivisor += 1
        if tripleDivisor == 3:
            break
        else:
            pass
    if tripleDivisor < 3:
        sumOfTripleDivisors = 0
    if sumOfTripleDivisors != 0 \
            and sumOfTripleDivisors % 2022 == 0 \
            and sumOfTripleDivisors != number:
        print(number, sumOfTripleDivisors)
        fiveNumbersCounter += 1
    if fiveNumbersCounter == 5:
        break
    else:
        pass
