# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# ВАРИАНТ 1:
# number = int(input('Введите число: '))
# print(f'{number:b}')

# ВАРИАНТ 2:
number = int(input('Введите число: '))
b = ''
while number > 0:
    b = str(number % 2) + b
    number = number // 2
print(b)
