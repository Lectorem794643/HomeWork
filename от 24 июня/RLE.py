string = input()
count = 1
symbol, i = 0, 0
for i in range(len(string) - 1):
    if symbol <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[symbol]
            print(count, string[i])
            count = 1
print(count, string[i])

# 010000100001111111110111110000000000000011111111

