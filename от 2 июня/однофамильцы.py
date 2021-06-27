counter = int(input())
namelist1, namelist2 = set(), set()
for i in range(counter):
    name = input()
    if name in namelist1:
        namelist2.add(name)
    else:
        namelist1.add(name)
result = namelist1 - namelist2
result = counter - len(result)
print(result)
