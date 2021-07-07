number_of_roads = int(input('введите количество маршрутов : '))
roads_X = 0
height_MAX = 0
for _ in range(number_of_roads):
    subway = int(input('введите количество тоннелей на маршруте : '))
    height_MIN = 1000000000
# не думаю, что существуют более высокие тоннели
    for __ in range(subway):
        height = int(input('введите высоту тоннеля : '))
        if height_MIN > height:
            height_MIN = height
    if height_MAX < height_MIN:
        height_MAX = height_MIN
        roads_X += 1
print(roads_X, height_MAX)
# CORRECT
