for digitOne in range(10):
    for digitTwo in range(10):
        number = int(f'12345{digitOne}6{digitTwo}8')
        if number % 17 == 0:
            print(number, number // 17)