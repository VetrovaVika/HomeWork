"""задача
написать функцию is_positive(num), которая возвращает True в случае,
если num положительное, и False во всех остальных случаях. 
Дан список чисел (только целые числа).
Напечатать 0 и отрицательные числа в списке применив, функцию is_positive"""
from random import randint
def is_positive(num):
    if num <= 0:
        return False
    else:
        return True
l = []
n = 10
for i in range(n):
    l.append(randint(-10, 10))
print(f"Первоначальный рандомный список чисел: {l}")
l_1 = []
for i in l:
    if is_positive(i):
        continue
    else:
        l_1.append(i)
print(f"0 и отрицательные числа из первого списка: {l_1}")

"""задача
написать функцию num_to_name_week(num_day_week), 
которая возвращает имя дня недели(строка)
ПРимер 
num_to_name_week(1) -> ‘Понедельник’"""
def num_to_name_week(num_day_week):
    day_week = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 
                5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
    if num_day_week < 1 or num_day_week > 7:
        print(False)
    else:
        for k in day_week:
            if k == num_day_week:
                print(f"{num_day_week} день недели это {day_week[k]}")
num_to_name_week(7)

"""задача
написать функцию для фигуры как на картинке: 
синие десятиугольники и красные пятиугольники
и решить задачу с применением этой функции"""
from turtle import *
from time import sleep
speed(10)
def drow_decagon(a: int, color_side: str):
    for i in range(1,11):
        color(color_side)
        forward(a)
        left(360/10)   
def drow_pentagon(b, color_side):
    for i in range(1,6):
        color(color_side)
        forward(b)
        left(360/5)
def drow_figure():
    for i in range (1, 11):
        drow_decagon(50, "blue")
        left(360/10)
    for i in range (1, 11):
        drow_pentagon(100, "red")
        left(360/10)
drow_figure()
sleep(10)

"""задача
написать ОДНУ функцию для фигур как на картинке.
и решить задачу с применением этой функции. порядок фигур не важен. 
Также должна быть возможность задавать произвольный размер и цвет через функцию"""        
from turtle import *
from time import sleep
speed(10)
def drow_figure(a: int, b: int, fill_color: str): # a - кол-во сторон, b - длина стороны, fill_color - цвет заливки 
    fillcolor(fill_color)
    begin_fill()
    for i in range(1, a+1):
        color(fill_color)
        forward(b)
        right(360/a)
    end_fill()
up()
goto (-200, 200)
down()
drow_figure(11, 20, "#a52a2a")
up()
goto (-100, 100)
down()
drow_figure(7, 30, "#fc03fc")
up()
goto (0, 0)
down()
drow_figure(3, 80, "#ff0000")
up()
goto (100, 100)
down()
drow_figure(4, 60, "#008000")
up()
goto (200, 200)
down()
drow_figure(8, 30, "#000000")
up()
goto (-100, -100)
down()
drow_figure(5, 50, "#0000ff")
up()
goto (-200, -200)
down()
drow_figure(9, 30, "#ffff00")
up()
goto (100, -100)
down()
drow_figure(6, 40, "#00ffff")
up()
goto (200, -200)
down()
drow_figure(10, 25, "#ffc0cb")
sleep(3)



