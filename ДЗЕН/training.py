row = row_counter = 1
n = int(input())
for myNumber in range(1, n + 1):
    print(myNumber, end=' ')
    row_counter -= 1
    if row_counter == 0:
        row += 1
        row_counter = row
        print()
