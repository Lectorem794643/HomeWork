string = str(input())
counter = len(string)
q = 0
while counter >= 0:
    print(string[q:-q])
    q += 1
    counter -= 2
# тут что-то сломано, но я не могу понять что(((