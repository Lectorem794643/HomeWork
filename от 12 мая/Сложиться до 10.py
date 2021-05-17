Number = int(input())
i, sum, line = 0, 0, 0
while Number != 0:
    i += 1
    sum += Number
    if sum == 10:
        line = i
    Number = int(input())
print(line)