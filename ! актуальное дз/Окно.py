milk_quantity_report = []
[milk_quantity_report.append(input('введите количество молока в бутылке : '))
 for n in range(int(input('введите количество бутылок : ')))]
Min, Max = int(input('введите мимальное допустимое количество молока : ')), \
           int(input('введите максимально допустимое количество молока : '))
[print(milk_quantity_report[i]) for i in range(len(milk_quantity_report)) if Min <= int(milk_quantity_report[i]) <= Max]
