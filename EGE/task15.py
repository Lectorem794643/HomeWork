for A in range(100, -1, -1):
    if all((2 * x + y != 70) or (x < y) or (A < x) for x in range(100) for y in range(100)):
        print(A)
        break

# читаем, что делает функция all
