i = 0
s = 0
while i != 1:
    a = float(input())
    if a >= 0:  # лишние скобки
        s += a  # отсутствует отбивка
    else:
        i += 1
print(s - (s / 100 * 5))  # лишняя отбивка

# в целом правильно, но нет явной проверки на цену товара (1000₽), наименование переменных и
# читаемость программы страдают, стоило бы так:
price = float(input())
total = 0
while (price > 0):
    if (price > 1000):
        total += price * 0.95
    else:
        total += price
    price = float(input())
print(total)
