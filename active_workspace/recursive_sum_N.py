# получаем на вход список уже найденных слагаемых summands,
# аргумент рекурсии n и предел верхнего значения суммы limit
def sum_of_n(summands, n, limit):
    # собираем список вариантов сложения, пока не дойдем до n < 1
    if n > 0:
        # перебираем все i от n до предела суммы с шагом -1
        for i in range(n, 0, -1):
            if i <= limit:
                # рекурсивно записываем подходящие i в список summands
                # и вызываем повторно для всех i от n - i до i
                # чтобы избежать повторов
                sum_of_n(summands + [i], n - i, i)
    else:
        # собрав все варианты перебора для n выводим собранную строку
        print(*summands, sep=' + ')


N = int(input())
sum_of_n([], N, N - 1)