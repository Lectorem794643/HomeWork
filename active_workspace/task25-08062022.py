for number in range(201455, 201470 + 1):
    numberOfDivisors = 0
    divisors = []
    for j in range(2, number // 2 + 1):
        if number % j == 0:
            numberOfDivisors += 1
            divisors.append(j)
        if len(divisors) > 2:
            break
    if len(divisors) == 2:
        print(1, *divisors, number)
