# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# number = (input('Введите число: '))
# result = 0
# for i in number:
#     if i != '.' and i != ',':   
#         result += int(i)
# print(f'Сумма цифр числа {number} равна {result}') 


float_num = (input('Введите число: '))
sum1 = 0
for i in float_num:
    if i.isdigit():
        sum1 += int(i)
print(f'Сумма цифр числа {float_num} равна {sum1}')