# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

entered_list = input('Введите числа через пробел: ').split()
my_list = list(map(int, entered_list))
prod_list = []
for i in range((len(my_list)+1)//2):
    prod_list.append(my_list[i] * my_list[len(my_list)-1-i])
print(f'{my_list} => {prod_list}')
