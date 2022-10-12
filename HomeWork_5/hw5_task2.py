# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random 
from random import randint, choice


# human vs human
def play_game(a, b, pl, mes):
    count = choose_first_move()
    print(f'\nПервым ходит {pl[count % 2]}')
    while a > 0:
        print(f'{pl[count % 2]}, {random.choice(mes)}')
        move = int(input())
        if move <= 0 or move >b:
            print(f'Можно взять не более {b}, текущее количество конфет: {a}')
            attempt = 3
            while attempt > 0:
                if move <= a and move <= b and move > 0:
                    break
                print(f'Попробуйте еще раз, у Вас еще {attempt} из трех попыток')
                move = int(input())
                attempt -= 1
            else: 
                return print(f'Попытки закончились. Игра окончена.')
        a -= move
        if a > 0:
            print(f'Осталось {a} конфет')
        else:
            print(f'Увы...конфет больше нет')
        count += 1
    return pl[not count % 2] 


# bot
def play_game2(a, b, pl, mes):
    count = choose_first_move()
    print(f'\nПервым ходит {pl[count % 2]}')
    while a > 0:
        if count % 2:
            move = a % (b + 1)
            if move == 0:
                move = randint(1, b)
            print(f'\nБот забрал {move} конфет')
        else:
            print(f'\n{pl[0]}, {choice(mes)}')
            move = int(input())
            if move < 1 or move >b:
                print(f'Можно взять не более {b}, текущее количество конфет: {a}')
            attempt = 3
            while attempt > 0:
                if move <= a and move <= b and move > 0:
                    break
                print(f'Попробуйте еще раз, у Вас еще {attempt} из трех попыток')
                move = int(input())
                attempt -= 1
            else: 
                return print(f'Попытки закончились. Игра окончена.')
        a -= move
        if a > 0:
            print(f'Осталось {a} конфет')
        else:
            print(f'Увы...конфет больше нет')
        count += 1
    return pl[not count % 2]


def choose_first_move():
        return randint(0, 1)


def introduce_player(d):
    if d == 0:
        player1 = input('Доброго времени суток! Введите Ваше имя: ')
        player2 = input('Доброго времени суток! Введите Ваше имя: ')
        return [player1, player2]
    else:
        player1 = input('Доброго времени суток! Введите Ваше имя: ')
        player2 = 'Botik'
        print(f'{player1} VS {player2}')
        return [player1, player2]


def game(d):
    if d == 0:
        winner = play_game(n, m, players, messages)
    elif d == 1:
        winner = play_game2(n, m, players, messages)
    if not winner:
        print('Мы остались без победителя...')
    else:
        print(f'У нас есть победитель! Все конфеты достаются {winner}')


greeting = ('Перед игрой, ознакомьтесь с условиями:'
'\nНа столе лежит 2021 конфета. Играют двое: human VS human или human VS bot, делая ход друг после друга.'
'\nЗа один ход можно забрать не более чем 28 конфет.'
'\nВыигрывает сделавший последний ход. Ему и достаются все конфеты.')

messages = ['Ваш ход', 'берите конфеты', 'Ваша очередь набирать сладости', 'возьмите конфеты']

print(greeting)
n = 2021
m = 28
lvl = int(input('Как желаете играть:'
'\n0 - human VS human'
'\n1 - human VS bot'
'\nВаш выбор: '))

players = introduce_player(lvl)
winner = game(lvl)
