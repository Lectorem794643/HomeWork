string = str(input())
counter = 0
new_counter = 0
for i in range(len(string)):
    if string[i] == 'о':
        new_counter += 1
    if string[i] != 'о':
        if counter < new_counter:
            counter = new_counter
        new_counter = 0
print(counter)

# CORRECT