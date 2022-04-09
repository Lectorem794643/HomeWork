counter, k = 0, 0
while counter < 5:
    k += 1
    m = 7000000 + k
    divisors = list()
    for numbers in range(2, m // 2 + 1):
        if m % numbers == 0:
            divisors.append(numbers)
    if len(divisors) < 3:
        counter += 1
        print(k)
