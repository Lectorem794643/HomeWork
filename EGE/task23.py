def transform_number(left_num, right_num):
    if left_num == right_num:
        return 1
    if left_num > right_num or left_num == 12:
        return 0
    return \
        transform_number(left_num + 1, right_num) + \
        transform_number(left_num + 2, right_num) + \
        transform_number(left_num * 3, right_num)


print(transform_number(2, 9) * transform_number(9, 19))

# Я хочу, чтобы ты разобрал это решение самостоятельно и объяснил мне, как это работает
