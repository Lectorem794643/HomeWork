list_of_numbers = []
for _ in range(int(input())):
    list_of_numbers.append(int(input()))
for A in range(len(list_of_numbers)):
    for B in range(A + 1, len(list_of_numbers)):
        if list_of_numbers[A] < list_of_numbers[B]:
            list_of_numbers[A], list_of_numbers[B] = list_of_numbers[B], list_of_numbers[A]
for i in range(len(list_of_numbers)):
    print(list_of_numbers[i])

# ПОЧИНИЛ
