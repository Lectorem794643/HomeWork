home_library = set()
home_library_counter = int(input())
class_library_counter = int(input())
for _ in range(home_library_counter):
    book = str(input())
    home_library.add(book)
for __ in range(class_library_counter):
    book = str(input())
    if book in home_library:
        print('YES')
    else:
        print('NO')
