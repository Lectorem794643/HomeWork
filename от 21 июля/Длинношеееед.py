print('программа ищет самую часто встречающуюся букву в веденном текстве')
alphabet = 'аА бБ вВ гГ дД еЕ ёЁ жЖ зЗ иИ йЙ кК лЛ мМ нН оО пП рР сС тТ уУ фФ хХ цЦ чЧ шШ щЩ ъЪ ыЫ ьЬ эЭ юЮ яЯ'.split()
text, counter, letter = str(input()), 0, ''
for symbol in alphabet:
    if text.count(symbol[0]) > counter:
        counter = text.count(symbol[0])
        letter = symbol[0]
    if text.count(symbol[1]) > 0:
        counter += text.count(symbol[1])
        letter = symbol[0]
print(counter, ' - количество раз, сколько встретился символ "', letter, '"')
# случайно решил одной программой два задения.
