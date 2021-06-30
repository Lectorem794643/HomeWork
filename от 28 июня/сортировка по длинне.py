text = []
number_of_rows = int(input())
for _ in range(number_of_rows):
    text.append(str(input()))
counter = 1
while counter < len(text):
    for i in range(len(text) - counter):
        if len(text[i]) > len(text[i + 1]):
            text[i], text[i + 1] = text[i + 1], text[i]
        counter += 1
for i in range(number_of_rows):
    print(text[i])
