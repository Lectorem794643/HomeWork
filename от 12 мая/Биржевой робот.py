price_yesterday = int(input())
price_today = int(input())
in_price, out_price, = 0, 0
bought = False
while price_today != 0:
    if bought == False:  # not bought !
        if price_yesterday > price_today:
            in_price = price_today
            bought = True
    elif bought == True:  # bought !
        if price_yesterday > price_today:
            out_price = price_today
            bought = False
    price_yesterday = price_today
    price_today = int(input())
print(in_price, out_price, out_price - in_price)

# WRONG
# Неправильная логика, тестируй как пример из задачи, так и свои кейсы
