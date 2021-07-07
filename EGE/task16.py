def recursion_f(n):  # до функций мы тоже скоро дойдем, станет понятнее
    if n <= 1:
        return 0
    if n % 2 == 1:
        return recursion_f(n - 1) + 3 * n ** 2
    return n // 2 + recursion_f(n - 1) + 2


print(recursion_f(49))

