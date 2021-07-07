num = 0
k = 1

for i in range(int(input())):
    numerator = int(input())
    denumerator = int(input())
    num = num * denumerator + numerator * k
    k *= denumerator

x = num
y = k

while y > 0:
    x, y = y, x % y

NX = num // x
KX = k // x
result = str(NX) + '/' + str(KX)
print(result)