word, number, letter = str(input()), int(input()), str(input())
if word[number - 1] == letter:
    print('ДА')
else:
    print('error')

# WRONG — Читай условие

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
allowedNumber = '1234567890'
favoriteString = str(input())
favoriteNumber = int(input())
favoriteLetter = str(input())
if (
    len(favoriteLetter) > 1 or len(favoriteString) < favoriteNumber or
    favoriteNumber < 0 or favoriteLetter not in alphabet
):
    print('ОШИБКА')
elif favoriteString[favoriteNumber - 1] == favoriteLetter:
    print('ДА')
else:
    print('НЕТ')