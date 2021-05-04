a=float(input())
if a%4==0 and a%100!=0:
    print('високосный')
elif a%400==0:
    print('високосный')
else:
    print('не високосный ')