list_of_numbers, difference = [], []
[list_of_numbers.append(int(input())) for i in range(int(input()))]
[[difference.append(i - j) for j in list_of_numbers] for i in list_of_numbers]
difference = list(set(difference))
difference.sort()
[print(i, end='\n') for i in difference]
