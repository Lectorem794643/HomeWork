for string_numbers in range(1, int(input()) + 1):
    string = str(input())
    for i in range(len(string)):
        if string[i:i+3] == 'кот':
            print(string_numbers, i + 1)
