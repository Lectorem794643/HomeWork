counter_day = int(input())
item = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']
for i in range(counter_day):
    print(item[i % 5])
# просто и работает
