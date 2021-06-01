N = int(input())
Sum = 0
for M in range(1, N):
    Sum += len(str(M))
    if Sum >= N:
        print(M)
        break
