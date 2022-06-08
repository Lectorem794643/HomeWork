with open('17.txt', 'r') as f:
    data = [int(x) for x in f.read().split('\n')]
counter, max_sum = 0, 0
for i in range(0, len(data) - 1):
    if (data[i] + data[i + 1]) % 9 == 0:
        counter += 1
        max_sum = max(max_sum, (data[i] + data[i + 1]))
print(counter, max_sum)