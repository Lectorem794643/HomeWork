heightSTR = input()
goden = 0
MINheight = 1000 # костыль конечно... но не знаю как иначе
MAXheight = 0
while heightSTR != '!':
    height = int(str(heightSTR)) # до цикла нам нужен str так как ждем " ! " но
    # после вхождения в цикл нам нужен int так как работа с числами
    if height > 150 and height < 190:
        goden += 1
    if height < MINheight:
        MINheight = height
    if height > MAXheight:
        MAXheight = height
    heightSTR = input()
print(goden)
print(MINheight, MAXheight)
