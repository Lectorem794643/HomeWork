rows, columns = int(input()), int(input())
table = [[0] * rows for _ in range(columns)]
# table = [[str(input()) for cell in range(columns)] for row in range(rows)]
for row in range(rows):
    for cell in range(columns):
        table[cell][row] = str(input())
print(table)

