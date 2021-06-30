list_of_numbers = []
for _ in range(int(input())):
    list_of_numbers.append(int(input()))
counter = 1
while counter < len(list_of_numbers):
    for i in range(len(list_of_numbers) - counter):
        if list_of_numbers[i] < list_of_numbers[i-1]:
            list_of_numbers[i], list_of_numbers[i-1] = list_of_numbers[i-1], list_of_numbers[i]
    counter += 1
for i in range(len(list_of_numbers)):
    print(list_of_numbers[i])

