line = [1]
for i in range(int(input('Введите N: '))):
    for j in range(len(line)):
        print(line[j], end=' ')
    print()
    new_line = [1]
    new_line += [line[numbers_position]+line[numbers_position+1]
                 for numbers_position in range(len(line)-1)] + [1]
    line = new_line
