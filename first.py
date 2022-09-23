# ============================ДЗ №1====================================
# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# n = int (input ('Введите число от 1 до 7:' ))
# if n == 6 or n == 7:
#     print ('да')
# else:
#      print ('нет')   

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for X in range (0,2):
#     for Y in range (0,2):
#         for Z in range (0,2):
#             print ( (not (X or Y or Z)) == (not X and not Y and not Z))

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int (input ('Введите координату х:' ))
# y = int (input ('Введите координату у:' ))
# if x > 0 and y > 0:
#     print ('Точка лежит в 1 плоскости')
# elif x < 0 and y > 0:
#     print ('Точка лежит во 2 плоскости')     
# elif x < 0 and y < 0:
#     print ('Точка лежит в 3 плоскости')
# elif x > 0 and y < 0:
#     print ('Точка лежит в 4 плоскости')
# else:
#     print ('Введите координаты отличные от нуля')    

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int (input ('Введите номер четверти плоскости: '))
# if n == 1:
#     print ('Возможные координаты точек: x > 0 и y > 0')
# elif n == 2:
#     print ('Возможные координаты точек: x < 0 и y > 0')   
# elif n == 3:
#     print ('Возможные координаты точек: x < 0 и y < 0')    
# elif n == 4:
#     print ('Возможные координаты точек: x > 0 и y < 0')
# else:
#     print ('Введите значение от 1 до 4')    

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Ax = int (input('Введите координату х первой точки: '))
# Ay = int (input('Введите координату y первой точки: '))
# Bx = int (input('Введите координату х второй точки: '))
# By = int (input('Введите координату y второй точки: '))
# C = float ((Ax - Bx)**2 + (Ay - By)**2)**0.5
# print ( C )

# =============================ДЗ №2===============================

# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# n = input(' Write number: ')
# sum = 0
# for i in n :
#     if i.isdigit():
#         sum+= int(i)
# print (sum)        

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# import math
# N = int (input ('Введите число: '))
# for i in range (1,N+1):
#     print (math.factorial(i), end=' ')

# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n= int (input ('Введите число: '))
# dict = {}
# for i in range (1,n+1):
#     dict[i] = (1+1/i)**i
# print (dict)
# print (sum(dict.values()))


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# from asyncore import read
# n = [-7, 2, 3, 4, -3, -2, 7]
# a = open ('text.txt' , 'r')
# pr = 1
# for i in a.read ().splitlines():
#     pr = pr * n [int(i)]
# print (pr)

# 5.Реализуйте алгоритм перемешивания списка.

# import random
# x = list(range(0,9))
# print (x)
# random.shuffle(x)
# print (x)

# ===================================ДЗ №3 =========================================
# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range (1, len(list), 2):
#     sum += list [i]
# print (sum)    

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 4, 5, 6]
# new_list = []
# for i in range (len(list)//2 + len(list) % 2):
#     new_list.append(list[i] * list[len(list) - 1 - i])
# print (new_list)    

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [float ('0.' + str(i).split('.')[1]) for i in [1.1, 1.2, 3.1, 5, 10.01] if '.' in str(i)]
# print(list)
# print (max(list)-min(list))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input("Введите число: "))
# new_str = ''
# while n > 0:
#     new_str = str(n%2) + new_str
#     n//=2
# print(new_str)    

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

# k=int(input("Введите k: "))
# listfibonacci = [0]*(k*2+1)
# print(listfibonacci)
# listfibonacci[k]=0
# listfibonacci[k+1]=1
# for i in range (k+2, len(listfibonacci)):
#     listfibonacci[i]= listfibonacci[i-2]+listfibonacci[i-1]
# for i in range (k,-1, -1):
#     listfibonacci[i]= listfibonacci[i+2]-listfibonacci[i+1]    
# print(listfibonacci) 
# 
# =======================================ДЗ № 4=========================================
# 
# 1. Вычислить число c заданной точностью d
# Пример: - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def check_number_simple(n: int):
#     i = 2
#     while n % i != 0 or i == n - 1:
#         i += 1
#     if i == n:
#         return n

# def fill_simple_list(n: int) -> list:
#     simple_list = [1]
#     for i in range(2, n+1):
#         if n % i == 0:
#             if check_number_simple(i) != None:
#                 simple_list.append(check_number_simple(i))
#             else:
#                 continue
#     return simple_list

# N = int(input('Введите число N: '))
# simple_list = fill_simple_list(N)
# print(simple_list)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# numbers = [1, 2, 2, 3, 3, 4, 5]
# def get_unique_numbers(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)
#     for number in unique_numbers:
#         list_of_unique_numbers.append(number)
#     return list_of_unique_numbers
# print(get_unique_numbers(numbers))

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# k = int(input('Введите коэффициент: '))
# a = int(random.randint(0,100))
# b = int(random.randint(0,100))
# c = int(random.randint(0,100))

# if a != 0:
#     first = (str(a) + "x^" + str(k) + " + ")
# else:
#     first = (str())

# if b != 0:
#     second = (str(b) + "x" + " + ")
# else:
#     second = (str())

# if c != 0:
#     third = (str(c) + " = 0")
# else:
#     third = (str())

# print(f'{first}{second}{third}')   


# =======================================ДЗ № 5=========================================

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# some_str = 'Знаем вероабвятно, как выжить, но не знаем, как жить вабв этойабв странеабв.'.split()
# new_str = (' '.join([word for word in some_str if 'абв'not  in word]))
# print (new_str)

# 2.Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import *
# import os

# welcome_text = ('Приветствую!\n'
#                 'Для начала я расскажу правила игры:\n'
#                 'Имеется 2021 конфета, вы берете их поочереди,\n'
#                 'причем, за один раз можно взять не больше 28 конфет.\n'
#                 'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
#                 'Начинаем!')
# print(welcome_text)

# message = ['твой ход', 'да бери уже', 'бери еще', 'не корову проигрываешь',
#            'забирай быстрее', 'начинай уже']

# def player_vs_player():
#     candies_total = 2021
#     max_take = 28
#     count = 0
#     player_1 = input('\nИгрок 1: ')
#     player_2 = input('\nИгрок 2: ')

#     print(f'\nИгроки {player_1} и  {player_2} начинайте!\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     x = randint(1, 2)
#     if x == 1:
#         lucky = player_1
#         loser = player_2
#     else:
#         lucky = player_2
#         loser = player_1
#     print(f'Поздравляю {lucky} ты ходишь первым !')

#     while candies_total > 0:
#         if count == 0:
#             step = int(input(f'\n{choice(message)} {lucky} = '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\nТы можешь взять только {max_take} конфет {lucky}, попробуй еще раз: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\nна кону еще {candies_total}')
#             count = 1
#         else:
#             print('Все кончились конфетки')

#         if count == 1:
#             step = int(input(f'\n{choice(message)}, {loser} '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\nТы можешь взять только {max_take} конфет {loser}, попробуй еще раз: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\nна кону еще {candies_total}')
#             count = 0
#         else:
#             print('Ну вот и все, закончились конфетки')

#     if count == 1:
#         print(f'{loser} ПОБЕДИЛ')
#     if count == 0:
#         print(f'{lucky} ПОБЕДИЛ')

# player_vs_player()

# def player_vs_bot():
#     candies_total = 2021
#     max_take = 28
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = 'Компьютер'
#     players = [player_1, player_2]
#     print(f'\nИгроки {player_1} и  {player_2} начинйте!\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     lucky = randint(-1, 0)

#     print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

#     while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Компьютер':
#             print(
#                 f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delenie = candies_total//28
#                 step = candies_total - ((delenie*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\nТвой ход,  {players[lucky%2]} \nНа кону {candies_total} {choice(message)}:  '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\nЗа ход можно взять {max_take} конфет, попробуй еще раз: '))
#         candies_total = candies_total - step

#     print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

# player_vs_bot()

# 3. Создайте программу для игры в ""Крестики-нолики"".

# game_matrix = [[None, None, None], [None, None, None], [None, None, None]]
# game_is_on = True
# while game_is_on:
#     # Крестик - латинская буква X, нолик - латинская буква O 
#     # Ходы принимаются в формате [0][0] = "X" или [2][1] = "О"
#     move = input()
#     exec("game_matrix" + move)
#     for row in game_matrix:
#         print(row)
    
#     reference_matrix = [
#         game_matrix[0],
#         game_matrix[1],
#         game_matrix[2],
#         [i[0] for i in game_matrix],
#         [i[1] for i in game_matrix],
#         [i[2] for i in game_matrix],
#         [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]],
#         [game_matrix[0][2], game_matrix[1][1], game_matrix[2][0]]
#     ]
#     for item in reference_matrix:
#         result = list(set(item))
#         if len(result) == 1 and result[0] != None:
#             print("Game over!")
#             game_is_on = False
#             break

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def encode(s):
#     encoding = "" # сохраняет выходную строку
#     i = 0
#     while i < len(s):
#         # подсчитывает количество вхождений символа в индексе `i`
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
#         # добавляет к результату текущий символ и его количество
#         encoding += str(count) + s[i]
#         i = i + 1
#     return encoding
# if __name__ == '__main__':
#     s = 'ABBCCCD'
#     print(encode(s)) 