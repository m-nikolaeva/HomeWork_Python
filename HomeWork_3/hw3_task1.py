# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

entered_list = input('Введите числа через пробел: ').split()
my_list = list(map(int, entered_list))
result = 0
for i in range(1, len(my_list), 2):
    result += my_list[i]
print(f'{my_list} -> на нечетных позициях элементы: {my_list[1::2]}, их сумма равна: {result}')
