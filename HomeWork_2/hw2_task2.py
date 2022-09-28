# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число N: '))
product = 1
list1 = []
for i in range(1, number+1):
    list1.append(str(product))
    product *= i
    # print(str(product))
print(', '.join(list1))
