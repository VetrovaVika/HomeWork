"""задача
Вывести на экран фигуру из звездочек:
*******
*******
*******
*******
(квадрат из n строк, в каждой строке n звездочек)
n - гарантируется, что целое число"""
while True:
    n = int(input("Введите число строк: "))
    if n <= 0:
     print("Число должно быть положительное!")
    else:
        for a in range(n):
            print("*"*n)
        break

"""задача
распечатайте все числа, которые делятся на 3 от start до
end(включительно) (start, end - могут быть перепутаны), 
start , end- гарантируется, что целые числа"""
start = int(input("Введите start = "))
end = int(input("Введите end = "))
if start > end:
    start, end == end, start
else:
    for i in range(start, end+1):
        if i%3==0:
            print(i)
        else:
            continue

"""задача
черепашка (увеличивающаяся разноцветная лестница)"""
from turtle import *
from time import *
a = 20
up()
setpos(-250, -250)
down()
col = 4
while a != 100:
    if col % 4 == 0: 
        pencolor('black')
    elif col % 4 == 1:
        pencolor('red')
    elif col % 4 == 2:
        pencolor('blue')
    elif col % 4 == 3:
        pencolor('yellow')    
    left(90)
    forward(a)
    right(90)
    forward(a)
    a += 10
    col += 1
sleep(3)

"""задача
черепашка (увеличивающийся квадрат)"""
from turtle import *
from time import *
a = 10
col = 3
while a != 500:
    if col % 3 == 0: 
        pencolor('red')
    elif col % 3 == 1:
        pencolor('green')
    elif col % 3 == 2:
        pencolor('blue')
    forward(a)
    left(90)
    a += 10
    col += 1
sleep(3)
    
"""задача
черепашка (китайская цветная стена)"""
from turtle import *
from time import *
a = 10
col = 3
up()
setpos(-250, 0)
down()
while a != 100:
    if col % 3 == 0: 
        pencolor('red')
    elif col % 3 == 1:
        pencolor('black')
    elif col % 3 == 2:
        pencolor('blue')
    forward(30)
    left(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    left(90)
    a += 10
    col += 1
sleep(3)



