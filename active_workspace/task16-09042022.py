def modder(a, b):
    if a < 1:
        return b
    else:
        return modder(a // 10, 10 * b + (a % 10))

for i in range(10, 1000):
    print(i, modder(i , 0))

# Замечаем, что алгоритм просто переворачивает число задом наперед, вызываем
# modder(1248163264 , 0), чтобы получить ответ

print(modder(1248163264 , 0))