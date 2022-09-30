# Реализуйте алгоритм перемешивания списка.

import random   

# Вариант 1:
# n = int(input("Введите количество элементов: "))
# fisrt_list = [i for i in range(n)]
# mixed_list = fisrt_list[:]
# random.shuffle(mixed_list)
# print(f'Первоначальный список: {fisrt_list} -> перемешанный список: {mixed_list}')

# ==============================

# Вариант 2:
n = int(input("Введите количество элементов: "))
fisrt_list = [i for i in range(n)]
mixed_list = fisrt_list[:]
for i in range(n):
    index_random = random.randint(0, n - 1)
    mixed_list[i], mixed_list[index_random] = mixed_list[index_random], mixed_list[i]
print(f'Первоначальный список: {fisrt_list} -> перемешанный список: {mixed_list}')

