# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки A:')
xa = int(input('x = '))
ya = int(input('y = '))
print('Введите координаты точки B:')
xb = int(input('x = '))
yb = int(input('y = '))

distance = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
print(f'A({xa},{ya}); B({xb},{yb}) -> {round(distance, 2)}')
