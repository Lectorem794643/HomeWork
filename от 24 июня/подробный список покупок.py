buy_list = []
for _ in range(int(input()) * 2):
    buy_list += [str(input())]
for i in range(0, len(buy_list), 2):
    print(buy_list[i], buy_list[i + 1])