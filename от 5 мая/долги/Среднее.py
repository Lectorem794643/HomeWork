# выводит среденее значение температуры
temperature = float(input())
SUMtemperature = 0
number = 0
while temperature > -300:  # >=
    SUMtemperature += temperature
    number += 1
    temperature = float(input())
print('средняя температура - ', SUMtemperature / number)

# CORRECT
