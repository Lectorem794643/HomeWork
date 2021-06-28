database = []
question_list = []
for _ in range(int(input())):
    database = [str(input())]
for __ in range(int(input())):
    question_list = [str(input())]
for i in range(len(database)):
    if question_list & database[i]:
        print(i)
# СЛОМАНО и не работает
