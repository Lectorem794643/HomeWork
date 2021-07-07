# Найти кота
STR1 = False  # что за название переменной?
line = input()
lineONE = 1
cat = 0
while line != 'СТОП':
    if STR1:
        if 'кот' in line:
            lineONE = line
            cat += 1
    if 'кот' in line:
        cat += 1
    line = input()
print(lineONE, cat)

# WRONG
# Тестируй по примерам
