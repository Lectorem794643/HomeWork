# считает строки до слова "спасибо" включительно
Lines = 0
STR = str(input())
while STR != 'Спасибо.':
    Lines += 1
    STR = str(input())
print('количество строк - ', Lines + 1)