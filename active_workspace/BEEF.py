os16 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "A", "B", "C", "D", "E", "F"]
#####################


def cnt(z, k):
    global os16
    i1 = os16.index(z)
    i2 = os16.index(z)
    c1 = 0
    c2 = 0
    while os16[i1] != k:
        if i1 == 15:
            i1 = 0
            c1 += 1
        print(i1, 'i1', c1, 'c1')
        i1 += 1
        c1 += 1
    c2 = 0
    while os16[i2] != k:
        if i2 == 0:
            i2 = 15
            c2 += 1
        i2 -= 1
        c2 += 1
        print(i2, 'i2', c2, 'c2')
    return min(c1, c2)


####################

st = input()
N = int(input())

S = 0

while len(st) > 3:
    print(st, N, S, "(string, N, S)")  # DEBUG
    mn = 65
    ind = "None"

    for i in range(0, 4):
        print(i, "i", len(st), 'length of string')  # DEBUG

        if i + 3 < len(st):
            # sn = cnt(st[i], "B")
            # print(sn, 'sn1')
            # sn = cnt(st[i + 1], "E")
            # print(sn, 'sn2')
            # sn += cnt(st[i + 2], "E")
            # print(sn, 'sn3')
            sn = cnt(st[i + 3], "F")
            print(sn, 'sn4')
            print(sn, "sn")  # DEBUG
            if sn < mn and sn <= N:
                print("entered")  # DEBUG
                N -= sn
                ind = i + 4

    print(ind, "ind")  # DEBUG
    if ind == "None":
        st = st[min(7, len(st) - 1):len(st)]
    else:
        S += 1
        st = st[min(ind, len(st) - 1):len(st)]

print(S)