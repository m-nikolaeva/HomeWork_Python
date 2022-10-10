# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def get_polinom(digits):
    digits = digits.strip().strip(' = 0')
    digits = digits.split(' + ')
    factor = {}
    for i in digits:
        a, *b = i.split(' * x ** ')
        if b:
            factor[int(b[0])] = int(a)
        else:
            if i.endswith('x'):
                a, *b = i.split(' * x')
                factor[1] = int(a)
            else:
                factor[0] = int(i)
    return factor


def sum_polinom(d, factor):
    for key in d:
        if not key in factor:
            factor[key] = 0
        factor[key] += d[key]
    return factor


with open('HomeWork_4/hw4_task4_01.txt') as f1:
    digits1 = f1.read()
with open('HomeWork_4/hw4_task4_02.txt') as f2:
    digits2 = f2.read()
    factor1 = get_polinom(digits1)
    factor2 = get_polinom(digits2)
    factor = {}
    factor = sum_polinom(factor1, factor)
    factor = sum_polinom(factor2, factor)
    res = ''
    max_num = max(factor.keys())
    for i, j in factor.items():
        res += str(j)
        if i != 0 and j != 0 and i != 1:
            res += ' * x ** '
            res += str(i)
            res += ' + '
        elif j == 0:
            continue
        elif i == 1:
            res += ' * x + '
        else:
            res += ' = 0'
            print(res)

file01 = 'HomeWork_4/hw4_task4_01.txt'
file02 = 'HomeWork_4/hw4_task4_02.txt'
file_task5 = 'HomeWork_4/hw4_task5.txt'

with open(file_task5, 'a') as data:
    data.write(f'{digits1} \n+\n{digits2} \n=> {res} \n')
