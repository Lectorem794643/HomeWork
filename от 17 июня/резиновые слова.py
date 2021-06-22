word = str(input())
if len(word) % 2 == 0:
    indent = int((len(word) - 2) / 2)
    indent2 = -1
    print(' ' * (indent + 1), word[int((len(word) - 2) / 2):int((len(word) - 2) / 2 + 2)])
    q = (indent2 + 1)
    for i in range(int((len(word) - 2) / 2)):
        q -= 1
        indent -= 2
        indent2 -= 1
        print(' ' * indent2, word[(indent2 + 1) - q], ' ' * indent, word[-(q - 1)])


#  синхрофазатрон
