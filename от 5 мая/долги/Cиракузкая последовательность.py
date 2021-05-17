number = int(input())
step = 0
while number != 1:
    if number % 2 == 0:
        number = number / 2
        step += 1
    else:
        number = 3 * number + 1
        step += 1
print(step)