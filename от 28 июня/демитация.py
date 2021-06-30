number_of_soldiers = int(input())
lucky = []
for i in range(number_of_soldiers):
    lucky.append(input())
k = int(input())
m = int(input())
# К и М потому что по уловию такие и я не слог придумать альт.название отражающие смысл переменной
while m:
    for i in range(number_of_soldiers - 1, -1, -1):
        if not (i + 1) % k:
            lucky.pop(i)
    number_of_soldiers = len(lucky)
    m -= 1
for i in lucky:
    print(i)
