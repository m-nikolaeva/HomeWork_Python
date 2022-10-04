# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# [5.12, 4.35, 1.01, 2.04, 6.17] => 0.34 - добавила пример с другими данными

# # ВАРИАНТ 1:
# entered_list = list(map(float, input('Введите числа через пробел: ').split()))
# my_list = [round(i % 1, 2) for i in entered_list if i % 1 != 0]
# print(f'{max(my_list)} - {min(my_list)} = {max(my_list) - min(my_list)}')


# ВАРИАНТ 2:
entered_list = input('Введите числа через пробел: ').split()
my_list =[]
min_ind = 0
max_ind = 0
for i in range(len(entered_list)):
    if float(entered_list[i]) % 1:
        j = round(float(entered_list[i]) % 1, 2)
        my_list.append(j)
for i in range(len(my_list)): 
    if my_list[i] < my_list[min_ind]:
        min_ind = i 
    if my_list[i] > my_list[max_ind]:
        max_ind = i 
    difference = round(float(my_list[max_ind]) - float(my_list[min_ind]), 2)
print(f'{my_list[max_ind]} - {my_list[min_ind]} = {difference}')
