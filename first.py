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

n = input(' Write number: ')
sum = 0
for i in n :
    if i.isdigit():
        sum+= int(i)
print (sum)        

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math
N = int (input ('Введите число: '))
for i in range (1,N+1):
    print (math.factorial(i), end=' ')

# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n= int (input ('Введите число: '))
dict = {}
for i in range (1,n+1):
    dict[i] = (1+1/i)**i
print (dict)
print (sum(dict.values()))


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from asyncore import read
n = [-7, 2, 3, 4, -3, -2, 7]
a = open ('text.txt' , 'r')
pr = 1
for i in a.read ().splitlines():
    pr = pr * n [int(i)]
print (pr)

# 5.Реализуйте алгоритм перемешивания списка.

import random
x = list(range(0,9))
print (x)
random.shuffle(x)
print (x)
