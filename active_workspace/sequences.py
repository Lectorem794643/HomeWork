sumOfNumbers = 0
for number in range(1024, 289213):
    limit = round(number ** 0.5)
    dividers = 0
    for i in range(2, limit + 1):
        if number % i == 0:
            dividers += 1
    if dividers == 0:
        sumOfNumbers += number
print(sumOfNumbers)\


