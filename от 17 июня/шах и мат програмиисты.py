letter = 'ABCDEFGHI'
size = int(input())
for i in range(size, 0, -1):
    for let in range(size):
        print(letter[let] + str(i), end=' ')
    print()
