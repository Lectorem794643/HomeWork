for A in range(100, -1, -1):
    if all((2 * x + 3 * y < 30) or (x + y >= A) for x in range(100) for y in range(100)):
        print(A)
        break

