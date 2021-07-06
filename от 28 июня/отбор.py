cool_magazine, good_students, good_good_students, new_students = list(), list(), list(), list()
for i in range(int(input('введите количество учеников'))):
    new_students = (str(input('введите фамилию и оценку ученика - ')))
    cool_magazine.append(new_students)
    if '4' in new_students:
        good_students.append(new_students)
    if '5' in new_students:
        good_good_students.append(new_students)
print('классный журкал:')
for i in range(len(cool_magazine)):
    print(cool_magazine[i])
print()
print('отличники:')
for i in range(len(good_good_students)):
    print(good_good_students[i])
print()
print('хорошисты:')
for i in range(len(good_students)):
    print(good_students[i])

