"""задача
распечатайте все числа (должны быть только положительные), 
которые делятся на 3 без остатка от start до end(включительно) 
(start, end - могут быть перепутаны), start , end- гарантируется, 
что целые числа. Найти в этом списке самое маленькое число, 
которое делится на три без остатка"""
start = int(input("Введите start = "))
end = int(input("Введите end = "))
if start < 0 and end < 0:
    print("start и end должны быть положительными")
else:
    if start > end:
        start, end == end, start
    else:
        for i in range(start, end+1):
            if i%3==0:
                print(i)
            else:
                continue
        if start%3==0:
            print("Минимальное число =", start)
        elif start%3==1:
            print("Минимальное число =", start+2)
        elif start%3==2:
            print("Минимальное число =", start+1)

"""Дан список элементов 1, 3, 22, 7, 12, 8, 2 
(могут быть какие-то другие значения, ввод данных делать не нужно)  
1. показать каждый элемент, последняя цифра которого 2
2. показать произведение чисел, последняя цифра которого 2""" 
multiplication = 1
for element in 1, 3, 22, 7, 12, 8, 2:
    # показать каждый элемент, последняя цифра которого 2
    if element%10==2 or element==2:
        # показать произведение чисел, последняя цифра которого 2
        multiplication = multiplication*element
        print(element)
    else:
        continue
print(f"Произведение = {multiplication}")

"""задача
черепашка (пунктирная линия)"""
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
    up()
    forward(10)
    down()
    a += 10
    col += 1
sleep(3)

