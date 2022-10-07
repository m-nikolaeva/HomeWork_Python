# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from collections import Counter
from random import randint


def my_list(n, m, v): 
    return [randint(m, v) for i in range(n)]


a = int(input('Введите количество чисел в списке: '))
b = int(input('Введите нижнюю границу чисел: '))
c = int(input('Введите верхнюю границу чисел: '))
entered_list = my_list(a, b, c)

# ВАРИАНТ 1, повторяющиеся элементы не попадают в новый список: [1,2,3,3,2,5]->[1,5] 
my_dict = Counter(entered_list)
res_list = [i for i in my_dict if my_dict[i] == 1]
print(f'Исходная последовательность: {entered_list}')
print(f'Неповторяющиеся элементы: {res_list}')

# ВАРИАНТ 2, все элементы попадают в новый список без повторений: [1,2,3,3,2,5]->[1,2,3,5]
# new_list = []
# [new_list.append(i) for i in entered_list if i not in new_list]
# print(f'{entered_list} ==> {new_list}')
















