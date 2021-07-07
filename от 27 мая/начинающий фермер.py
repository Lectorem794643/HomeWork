calfPrice, cowPrice, bullPrice = 5, 10, 20
credit = int(input())
herd = int(input())
for bullQuantity in range(1, credit // bullPrice + 1):
    for cowQuantity in range((credit - bullQuantity * bullPrice) // cowPrice + 1):
        calfQuantity = herd - bullQuantity - cowQuantity
        if bullQuantity * bullPrice + cowQuantity * cowPrice + calfQuantity * calfPrice == credit:
            print(bullQuantity, cowQuantity, calfQuantity)

# CORRECT
# Цены хорошо бы выносить в константы
