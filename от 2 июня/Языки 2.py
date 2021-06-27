group = set()
pause = set()
n = int(input())
m = int(input())
k = int(input())
counter = 0
for _ in range(n + m + k):
    name = input()
    if name in group:
        counter += 1
        pause.add(name)
    group.add(name)
if (n == k == m) and len(group) == n:
    print('NO')
else:
    if len(pause) + counter > 0:
        if (len(pause) + counter) % 2 != 0:
            print((len(pause) + counter) % 2)
        else:
            print((len(pause) + counter) // 2)
    else:
        print('NO')
