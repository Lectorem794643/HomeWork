MyString = str(input('введите данные : ')).split()
string = [print('*' * int(MyString[i])) for i in range(len(MyString))]
# 3 7 1 10 8
