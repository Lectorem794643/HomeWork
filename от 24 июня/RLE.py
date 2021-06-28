string = input()
cout = 1
symbol, i = 0, 0
for i in range(len(string)-1):
    if symbol <= len(string):
        if string[i] == string[i + 1]:
            cout += 1
        else:
            a = string[symbol]
            print(cout, string[i])
            cout = 1
print(cout, string[i])

# 010000100001111111110111110000000000000011111111

