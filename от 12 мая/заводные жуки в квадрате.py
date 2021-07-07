side_square = float(input())
speed = float(input())
i = 0
while side_square - speed > 0.01:
    side_square = ((side_square - speed) ** 2 + speed ** 2) ** 0.5
    i += 1
print(i)

# CORRECT 0.8
# используй abs
# не хватает проверки, что side_square > speed
