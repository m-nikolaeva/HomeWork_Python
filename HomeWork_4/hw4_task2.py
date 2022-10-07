# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# ==================================================
# Теория: Как разложить число на простые множители.
# Для того чтобы разложить число на простые множители нужно, для начала, поделить его на 2.
# Если число разделится на 2 без остатка, то 2 – это первый множитель.
# Далее полученный результат опять делим на 2, если число разделится на 2 без остатка,
# то второй множитель тоже 2. Если же при делении получается остаток, то пробуем делим на 3, 4, ... num,
# до тех пор число не разделится без остатка.

import math


def primefactors(n):
    my_list = []
    for i in range(2, int(math.sqrt(n))+1):
        while (n % i == 0):
            my_list.append(i)
            n = n / i
    if n > 1:
        my_list.append(int(n))
    return my_list


number = int(input('Введите натуральное число N: '))
print(f'Список простых множителей числа {number}: {primefactors(number)}')
