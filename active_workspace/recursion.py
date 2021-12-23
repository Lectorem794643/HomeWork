def f(n):
    g24 = -141107
    f24 = -924437
    if n == 1:
        return 1
    elif n == 25:
        return f24 - 2 * g24
    else:
        return f(n - 1) - 2 * g(n - 1)


def g(n):
    g24 = -141107
    f24 = -924437
    if n == 1:
        return 1
    elif n == 25:
        return f24 + g24 + 25
    else:
        return f(n - 1) + g(n - 1) + n


result = g(36)
print('G(36) =', result)
sumOfDigits = 0
while result > 0:
    sumOfDigits += result % 10
    result = result // 10
print('Sum of digits:', sumOfDigits)