# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат. (¬ отрицание, ∧ и, ∨ или)


x = int(input('Введите значение X: '))
y = int(input('Введите значение Y: '))
z = int(input('Введите значение Z: '))

a = not (x or y or z)
b = not x and not y and not z
if a == b:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')

# ===========================================
# x = float(input('Enter X: '))
# y = float(input('Enter Y: '))
# z = float(input('Enter Z: '))

# a = not(x or y or z)
# b = not x and not y and not z

# print(a == b)


# #============================

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not (x or y or z) == (not x and not y and not z):
#                 print(x, y, z)