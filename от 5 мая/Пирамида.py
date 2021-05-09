h = int(input())
a = 1
for _ in range(h):
    print(' ' * h, '*' * a, ' ' * h)
    a += 2
    h -= 1
