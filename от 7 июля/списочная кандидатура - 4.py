numbers_for_squaring = str(input()).split()
MAGICIAN = [print(int(numbers_for_squaring[i]) ** 2, end=' ') for i in range(len(numbers_for_squaring)) if
            (int(numbers_for_squaring[i]) ** 2) % 10 != 9]
