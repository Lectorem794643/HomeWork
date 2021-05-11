i = 0
s = 0
while i != 1:
    a = float(input())
    if (a) >= 0:
        s +=a
    else:
        i += 1
print( s - (s / 100 * 5) )