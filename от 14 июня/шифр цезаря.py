key = int(input('введите ключ шифра : '))
text = str(input('введите шифрируемое сообщение : '))
cipher = ''
for I in range(len(text)):
    if I == ' ':
        cipher += ' '
    # проверка на пробел как символ
    if I == '!':
        cipher += '!'
    # проверка на ! как символ
    if I == ',':
        cipher += ','
    # проверка на , как символ
    if ((ord(text[I])) + key) > 1103:
        cipher += (chr(1071 + ((ord(text[I])) + key) - 1103))
        # так реализовал "закольцованность" алфавита
    if ((ord(text[I])) + key) <= 1103:
        cipher += (chr(ord(text[I]) + key))
        # штатный перевод, без кольца
print(cipher)
# сверху косячная программа с попыткой сделать знаки но она чет не работает как надо
# но вот буквы всегда правильные (нашел в интрнете онлайн калькулятор шира и проверял) -
# калькулятор - https://planetcalc.ru/1434/
# не понимаю что не так со знаками

# снизу программа-помошник для выяснения номера символа

text = ' '
for _ in range(len(text)):
    print(ord(text[_]))
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# абвгдежзийклмнопрстуфхцчшщъыьэюя
# АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ
