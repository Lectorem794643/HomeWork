saying = ['-'.join(map(str.upper, i)) for i in (str(input())).split()]
[print(saying[word], end=' ') for word in range(len(saying))]
# Мир будет наш
