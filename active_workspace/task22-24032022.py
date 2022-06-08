for i in range(-10000000, 10000000):
    x = i
    a = 0
    b = 0
    while x > 0:
        c = x % 2
        if c == 0:
            a += 1
        else:
            b += 1
        x //= 10
    if a == 2 and b == 3:
        print(i)
        break
