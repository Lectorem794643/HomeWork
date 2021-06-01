spaceship = int(input())
countdown = 0
for _ in range(spaceship):
    sec = countdown
    for _ in range(sec + 1):
        print('осталось секунд:', sec)
        sec -= 1
    print('Пуск!')
    countdown += 1
