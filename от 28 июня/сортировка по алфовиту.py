text = []
number_of_rows = int(input())
for i in range(number_of_rows):
    text.append(input())  # почему без str()
for A in range(number_of_rows):
    for B in range(A + 1, number_of_rows):
        if text[A] > text[B]:
            text[A], text[B] = text[B], text[A]
for i in range(number_of_rows):
    print(text[i])
