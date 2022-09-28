# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

# a = int(input('Введите цифру от 1 до 7: '))
# if a == 6 or a == 7:
#     print(a, '->', 'выходной')
# elif 1 <= a <= 5:
#     print(a, '->', 'не выходной')
# else:
#     print('некорректный ввод. попробуйте снова.')


num = int(input('Input the number of the day: '))

while num < 1 or num > 7:
    num = int(input('Wrong input. Try again here: '))

if num == 6 or num == 7:
    print('Yes')
else:
    print('No')