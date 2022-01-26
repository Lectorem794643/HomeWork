with open('24_demo.txt', 'r') as file:
    data = file.read()
maxLength = 1
countLength = 1
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        countLength += 1
        maxLength = max(maxLength, countLength)
    else:
        countLength = 1
print(maxLength)

# А вот как можно написать эту программу в одну строку:
# print(max(map(len, data.replace('XX', ' ').replace('YY', ' ').replace('ZZ', ' ').split())) + 1)
