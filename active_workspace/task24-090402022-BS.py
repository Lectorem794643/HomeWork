with open('24.txt') as file:
    data = file.read().replace('AB', '*').\
        replace('AC', '*').\
        replace('A', ' ').\
        replace('B', ' ').\
        replace('C', ' ').\
        split(' ')
print(max(len(x) for x in data))