a=float(input())
b=float(input())
run=input()
if run == '+' or run == '-' or run == '*' or run == '/':
    if run == '+':
        print(a+b)
    elif run == '-':
        print(a-b)
    elif run == '*':
        print(a*b)
    elif run == '/' and b != 0 :
        print(a/b)
    else:
        print('error')
else:
    print('error')