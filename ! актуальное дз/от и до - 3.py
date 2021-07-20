numbers = [int(i) for i in input().split()]
limit = [int(i) for i in input().split()]
exponentiation = [i ** 2 for i in (numbers[limit[0]:limit[1] + 1])]
print(sum(exponentiation))
