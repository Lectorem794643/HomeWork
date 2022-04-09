maxa = 0
for i in range(100000):
    x = i
    a, b = 1, 0
    while x > 0:
        d = x % 10
        a *= d
        if d > 5:
            b += d
        x //= 10
    if a == 6300:
        maxa = max(maxa, b)
print(maxa)
