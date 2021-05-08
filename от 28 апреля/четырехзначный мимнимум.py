a=int(input())
c1=a//1000
c2=(a-c1*1000)//100
c3=(a-c1*1000-c2*100)//10
c4=a-c1*1000-c2*100-c3*10
# разбил число на цифры
min=10000
if min<c1:
    min=min
else:
    min=c1
if min<c2:
    min=min
else:
    min=c2
if min<c3:
    min=min
else:
    min=c3
if min<c4:
    min=min
else:
    min=c4
#таким образом, нашел самое маленькое число
min2=10000
if min2>c1 and c1 != min:
    min2=c1
else:
    min2=min2
if min2>c2 and c2 != min:
    min2=c2
else:
    min2=min2
if min2>c3 and c3 != min:
    min2=c3
else:
    min2=min2
if min2>c4 and c4 != min:
    min2=c4
else:
    min2=min2
#таким образом нашел второе по возрастанию число.
min3=10000
if min3>c1 and c1 != min and c1 != min2:
    min3=c1
else:
    min3=min3
if min3>c2 and c2 != min and c2 != min2:
    min3=c2
else:
    min3=min3
if min3>c3 and c3 != min and c3 != min2:
    min3=c3
else:
    min3=min3
if min3>c4 and c4 != min and c4 != min2:
    min3=c4
else:
    min3=min3
#нашел третье по возрастанью
min4=10000
if min4>c1 and c1 != min and c1 != min2 and c1 != min3:
    min4=c1
else:
    min4=min4
if min4>c2 and c2 != min and c2 != min2 and c2 != min3:
    min4=c2
else:
    min4=min4
if min4>c3 and c3 != min and c3 != min2 and c3 != min3:
    min4=c3
else:
    min4=min4
if min4>c4 and c4 != min and c4 != min2 and c4 != min3:
    min4=c4
else:
    min4=min4
print(str(min) + str(min2) + str(min3) + str(min4))

#жутко не рационально, но вроде работает корректно