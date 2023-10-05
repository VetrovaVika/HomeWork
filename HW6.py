"""задача
Дана пицца 8 кусочков. Доступны команды:
1. print(‘Взять кусок’)
2. print(‘съесть кусок’)
написать программу, симулующую поедание кусочков пиццы (По желанию можно анимацию 
убывание кусочков пиццы добавить)"""

print("Ням-ням, пицца!")
pizza = 8
while pizza != 0:
    print('Взять кусок')
    print('Съесть кусок')
    pizza -= 1
    print(f"Осталось {pizza} кусочков")
    if pizza != 0:
        print("""Хочу ещё кусочек!
              """)
    elif pizza == 0:
        print("Пицца кончилась :(")

"""задача
Дано число n. Вывести степени этого числа с 1 по 10
пример
n=2
2^1=2
2^2=4
…
2^9=512
2^10 = 1024"""

n = int(input("Введите число "))
t = 1
while t != 11:
    print(f"{n}^{t}={n**t}")
    t += 1

"""Написать программу для черепашки (12 конечная звезда с кружком внутри)"""
from turtle import *
from time import *
turn = 11
while turn !=0:
    forward(100)
    left(180-180/11)
    turn -= 1
sleep(3)

"""Написать программу для черепашки (квадрат в квадрате)"""
from turtle import *
from time import *
turn = 10
a = 20
while turn != 0:
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    turn -= 1
    a += 10
    up()
    right(90)
    forward(5)
    right(90)
    forward(5)
    left(180)
    down()
sleep(5)
