def splitter(string_to_split, string_splitted=[]):
    if len(string_to_split) == 0:
        return string_splitted
    if len(string_splitted) == 0 or string_to_split[0] != string_splitted[-1][0]:
        return splitter(string_to_split[1:], string_splitted + [string_to_split[0]])
    return splitter(string_to_split[1:], string_splitted[:-1] + [string_splitted[-1] + string_to_split[0]])


myString = '11111000010101010101110100010010101111010010000111110010010010110001011'
zippedStringList = [digit[0] + '→' + str(len(digit)) for digit in splitter(myString)]
print('Это список, разделенный по одинаковым символам:\n', splitter(myString),
      '\nЭто список с идентификаторами символов и их количеством:\n', zippedStringList,
      '\nА это строка, склеенная через ;:\n', '; '.join(zippedStringList))
