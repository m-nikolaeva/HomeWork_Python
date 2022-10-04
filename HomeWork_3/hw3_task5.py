# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] F−n = (−1)n+1Fn [Негафибоначчи]

# ВАРИАНТ 1:
def negafibonacci(n):
    list_negafib = [0]
    if n == 0:
        return list_negafib
    elif n == 1:
        list_negafib = [1, 0, 1]
        return list_negafib
    else:
        list_negafib = [-1, 1, 0, 1, 1]
        fib1 = fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        list_negafib.append(fib2)
        list_negafib.insert(0, (fib2 * (-1) ** i))
    return list_negafib


k = int(input("Введите число: "))
print((f'Для k = {k} список выглядит так:\n{negafibonacci(k)}'))



# ВАРИАНТ 2:
# n = int(input("Введите число: "))
# list_negafib = [0, 1]
# for i in range(2, n + 1):
#     list_negafib.append(list_negafib[i-1] + list_negafib[i-2])
# for i in range(n):
#     list_negafib.insert(0, list_negafib[1] - list_negafib[0])
# print(f'Для k = {n} список выглядит так:\n{list_negafib}')
