m, n = int(input()), int(input())
for b in range(1, n + 1):
    for a in range(1, m + 1):
        print(a/b, end=' ')
    print()