whitelist, blacklist = [], []
for _ in range(int(input())):
    whitelist += [str(input())]
for __ in range(int(input())):
    blacklist += [str(input())]
for question in whitelist:
    if question in blacklist:
        print(question)
