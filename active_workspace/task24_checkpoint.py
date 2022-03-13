with open('24_demo (1).txt') as file:
    data = file.read().split('X')
print(max(map(len, [Y.split('Z') for Y in data])))