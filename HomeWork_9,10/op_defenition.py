import re
from calc_op import *


def in_put_int(msg):
    msg = re.sub(r'[\s=s]', '', msg)
    int_reg = re.fullmatch(r'/+[+-]?\d+[+-/*]\d+', msg)
    rac_reg = re.fullmatch(r'/+[+-]?\d+/\d+[+/*-]\d+/\d+', msg)
    comp_reg = re.fullmatch(r'/+\(([+-]?\d+|[+-]?\d+i|[+-]?\d+[+-]\d+i|[+-]?\d+i[+-]\d+|[+-]?\d+[+-]i)\)'
                            r'[+/*-]\(([+-]?\d+|[+-]?\d+i|[+-]?\d+[+-]\d+i|[+-]?\d+i[+-]\d+|[+-]?\d+[+-]i)\)', msg)
    print(msg)
    print(comp_reg)
    if not int_reg and not rac_reg and not comp_reg:
        return 'что вы от меня хотите? я это не умею!'
    if int_reg:
        x = re.split(r'([+-]?\d+)[+*/-]\d+', msg)[1]
        act = re.split(r'[+-]?\d+([+*/-])\d+', msg)[1]
        y = re.split(r'[+-]?\d+[+*/-](\d+)', msg)[1]
        result = calc_integer(int(x), act, int(y))
        return 'вычисление целых чисел: ' + str(result)
    if rac_reg:
        act = re.split(r'\d+/\d+([+/*-])\d+/\d+', msg)[1]
        num_spl = re.split(r'[\+\/\*\-]', msg)
        my_list = [x for x in num_spl if x]
        a, b, c, d = my_list
        result = calc_fraction(int(a), int(b), act, int(c), int(d))
        return 'вычисление рациональных чисел: ' + str(result)
    if comp_reg:
        comp = re.split(r'[\)\(i]', msg)
        print(comp)
        comp_first = comp[1]
        a = re.split(r'([+-]?\d+)[+-]\d+', comp_first)[1]
        b = re.split(r'[+-]?\d+\+?(-?\d+)', comp_first)[1]
        print(comp_first, type(comp_first), a, b)
        comp_act = comp[3]
        print(comp_act, type(comp_act))
        comp_two = comp[4]
        c = re.split(r'([+-]?\d+)[+-]\d+', comp_two)[1]
        d = re.split(r'[+-]?\d+\+?(-?\d+)', comp_two)[1]
        print(comp_two, type(comp_two), c, d)
        result = complex_num(int(a), int(b), comp_act, int(c), int(d))
        return 'вычисление комплексных чисел: ' + str(result)
        