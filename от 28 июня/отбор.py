cool_magazine = []
good_students = []
for i in range(int(input())):
    new_students = [str(input()), int(input())]
    cool_magazine.append(new_students)
    # изучай проверку на вхождение в кортеж
    if new_students in (4, 5):
        good_students.append(new_students)
print(cool_magazine)
print(good_students)
