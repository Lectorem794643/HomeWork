n = int(input())
battlefield = []
for i in range(n):
    battlefield.append(input())
for i in battlefield:
    if 'xxx' in i:
        print('X - WIN!')
        break
    if 'ooo' in i:
        print('0 - WIN!')
        break
else:
    for x in range(n):
        s = ''
        for c in battlefield:
            s += c[x]
        if 'xxx' in s:
            print('X - WIN!')
            break
        if 'ooo' in s:
            print('0 - WIN!')
            break
    else:
        print('-')
