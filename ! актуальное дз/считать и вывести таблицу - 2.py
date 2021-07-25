a = []
row, column = int(input()), int(input())
for i in range(row):
    b = []
    for j in range(column):
        b.append(input())
    a.append(b)
for i in a:
    for j in range(column - 1):
        print(i[j], end='\t')
    print(i[-1])
print()
for i in range(column):
    for j in range(row - 1):
        print(a[j][i], end='\t')
    print(a[-1][i])
