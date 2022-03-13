# Ученица составляет 5-буквенные слова из букв ГЕПАРД.
# При этом в каждом слове ровно одна буква Г, слово не может
# начинаться на букву А и заканчиваться буквой Е.
# Какое количество слов может составить ученица?

from itertools import *
maxSum = 0
for words in product('12', repeat=16):
    mySum = 0
    if words.count('2') == 4 and words.count('1') == 12:
        myString = ''.join(words)
        while '11' in myString:
            if '112' in myString:
                myString = myString.replace('112', '7')
            else:
                myString = myString.replace('11', '3')
        for i in range(len(myString)):
            mySum += int(myString[i])
        maxSum = max(maxSum, mySum)
print(maxSum)

# Читай https://python-scripts.com/itertools :: product и repeat
