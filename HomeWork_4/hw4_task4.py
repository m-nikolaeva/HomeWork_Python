# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import random


def write_file(st):
    with open('HomeWork_4/hw4_task4_01.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 100)


def ending_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst


def ending_str(sp):
    sked = sp[::-1]
    wr = ''
    if len(sked) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(sked)):
            if i != len(sked) - 1 and sked[i] != 0 and i != len(sked) - 2:
                wr += f'{sked[i]} * x ** {len(sked)-i-1}'
                if sked[i+1] != 0:
                    wr += ' + '
            elif i == len(sked) - 2 and sked[i] != 0:
                wr += f'{sked[i]} * x'
                if sked[i+1] != 0:
                    wr += ' + '
            elif i == len(sked) - 1 and sked[i] != 0:
                wr += f'{sked[i]} = 0'
            elif i == len(sked) - 1 and sked[i] == 0:
                wr += ' = 0'
    return wr


k = int(input('Введите натуральную степень k = '))
factor = ending_mn(k)
write_file(ending_str(factor))


# создание списка случайных чисел указанного диапазона с указанной степенью уравнения
# def ending_list(k, m, n):
#     return [randint(m, n) for i in range(k + 1)]


# # создание и форматирование многочлена на основании списка чисел
# def ending_polynom(entered_list):
#     polynom_list = []
#     for i in range(len(entered_list)):
#         if entered_list[-1 - i] != 0:
#             polynom_list.insert(0, str(entered_list[-1 - i]) + ' * x**' + str(i))
#             polynom_str = ' + '.join(polynom_list)
#             polynom_str += ' = 0'
#             polynom_str = polynom_str.replace('1 *', ' ')
#             polynom_str = polynom_str.replace('**1', '')
#             polynom_str = polynom_str.replace('x**0', '1')
#             polynom_str = polynom_str.replace('* 1', '')
#         if polynom_str[0] == '1' and polynom_str[1] == ' * ':
#             n = 2
#             polynom_str = polynom_str[n:]
#     return polynom_str


# k = int(input('Введите степень уравнения: '))
# m = int(input('Введите нижнюю границу чисел: '))
# n = int(input('Введите верхнюю границу чисел: '))
# entered_list = ending_list(k, m, n)
# polynom_list = ending_polynom(entered_list)

# print(entered_list)
# print(ending_polynom(entered_list))

# with open('/Users/marina/Documents/HomeWork_Python/HomeWork_4/hw4_task4_01.txt', 'a') as data:
#     data.write(f'\n{ending_polynom(entered_list)}')
