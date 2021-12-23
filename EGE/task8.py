# Ученица составляет 5-буквенные слова из букв ГЕПАРД.
# При этом в каждом слове ровно одна буква Г, слово не может
# начинаться на букву А и заканчиваться буквой Е.
# Какое количество слов может составить ученица?

from itertools import *
numberOfWords = 0
for words in product('ГЕПАРД', repeat=5):
    if words.count('Г') == 1 and words[0] != 'А' and words[-1] != 'Е':
        numberOfWords += 1
print(numberOfWords)

# Читай https://python-scripts.com/itertools :: product и repeat
