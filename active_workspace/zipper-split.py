def splitter(string_to_split, string_splitted=[]):
    if len(string_to_split) == 0:
        return string_splitted
    if len(string_splitted) == 0 or string_to_split[0] != string_splitted[-1][0]:
        return splitter(string_to_split[1:], string_splitted + [string_to_split[0]])
    return splitter(string_to_split[1:], string_splitted[:-1] + [string_splitted[-1] + string_to_split[0]])


myString = '1110101001010100'
zippedStringList = [digit[0] + '→' + str(len(digit)) for digit in splitter(myString)]
print(splitter(myString), '\n', zippedStringList)
zippedString = '; '.join(zippedStringList)
print(zippedString)
