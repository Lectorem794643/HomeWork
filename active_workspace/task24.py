# Задача 4
# from re import findall
# with open('24.txt', 'r') as file4:
#     data = file4.read()
# match = findall(r'A.', data)
# frequent = max(set(match), key=match.count)
# print(frequent[1])

# Задача 5
from re import finditer
with open('24_5.txt', 'r') as file5:
    data = file5.read()
    file5.close()
match = finditer(r'([A-Z]).\1', data)
gates, stats = [], []
for match_obj in match:
    gates.append(match_obj.group())
for strings in gates:
    stats.append(strings[1])
print(max(set(stats), key=stats.count))

