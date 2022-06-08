import openpyxl
file = openpyxl.load_workbook(filename='18 (3).xlsx')
sheet = file['Лист1']
data = [v[0].value for v in sheet['A1:A500']]
numSum, maxSum = data[0], 0
for i in range(len(data) - 1):
    if abs(data[i] - data[i + 1]) > 8:
        numSum = 0
    else:
        numSum += data[i + 1]
        maxSum = max(maxSum, numSum)
print(int(maxSum))
