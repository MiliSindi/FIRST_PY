# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int (input ('Введите число от 1 до 7:' ))
if n == 6 or n == 7:
    print ('да')
else:
     print ('нет')   



# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for X in range (0,2):
    for Y in range (0,2):
        for Z in range (0,2):
            print ( (not (X or Y or Z)) == (not X and not Y and not Z))

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int (input ('Введите координату х:' ))
y = int (input ('Введите координату у:' ))
if x > 0 and y > 0:
    print ('Точка лежит в 1 плоскости')
elif x < 0 and y > 0:
    print ('Точка лежит во 2 плоскости')     
elif x < 0 and y < 0:
    print ('Точка лежит в 3 плоскости')
elif x > 0 and y < 0:
    print ('Точка лежит в 4 плоскости')
else:
    print ('Введите координаты отличные от нуля')    


# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

n = int (input ('Введите номер четверти плоскости: '))
if n == 1:
    print ('Возможные координаты точек: x > 0 и y > 0')
elif n == 2:
    print ('Возможные координаты точек: x < 0 и y > 0')   
elif n == 3:
    print ('Возможные координаты точек: x < 0 и y < 0')    
elif n == 4:
    print ('Возможные координаты точек: x > 0 и y < 0')
else:
    print ('Введите значение от 1 до 4')    

     

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

Ax = int (input('Введите координату х первой точки: '))
Ay = int (input('Введите координату y первой точки: '))
Bx = int (input('Введите координату х второй точки: '))
By = int (input('Введите координату y второй точки: '))
C = float ((Ax - Bx)**2 + (Ay - By)**2)**0.5
print ( C )