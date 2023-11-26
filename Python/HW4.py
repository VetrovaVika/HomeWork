#задача 1
"""даны 3 числа, распечатать в порядке возрастания"""

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
if num1 < num2 < num3 : print(num1, num2, num3)
if num3 < num2 < num1 : print(num3, num2, num1)
if num2 < num1 < num3 : print(num2, num1, num3)
if num2 < num3 < num1 : print(num2, num3, num1)
if num1 < num3 < num2 : print(num1, num3, num2)
if num3 < num1 < num2 : print(num3, num1, num2)

#задача 2
"""Написать программу для следующей задачи
работают 3 сотрудника, у них есть оклад в размере 300.
Если сотрудник выполнит 50 и более продаж, то получит премию в 
размере 30% от оклада, если более 75, то получит премию в размере 65%
от оклада, а если 100, то - 100% от оклада"""

employee1 = int(input("Сколько продаж выполнил первый сотрудник? "))
employee2 = int(input("Сколько продаж выполнил второй сотрудник? "))
employee3 = int(input("Сколько продаж выполнил третий сотрудник? "))
salary = 300
# employee1
if employee1 < 50 : pay1 = salary
if 50 <= employee1 < 75 : pay1 = salary*0.3+salary
if 75 <= employee1 < 100 : pay1 = salary*0.65+salary
if employee1 >= 100 : pay1 = salary+salary
print(f"Зарплата первого сотрудника {pay1}")
# employee2
if employee2 < 50 : pay2 = salary
if 50 <= employee2 < 75 : pay2 = salary*0.3+salary
if 75 <= employee2 < 100 : pay2 = salary*0.65+salary
if employee2 >= 100 : pay2 = salary+salary
print(f"Зарплата второго сотрудника {pay2}")
# employee3
if employee3 < 50 : pay3 = salary
if 50 <= employee3 < 75 : pay3 = salary*0.3+salary
if 75 <= employee3 < 100 : pay3 = salary*0.65+salary
if employee3 >= 100 : pay3 = salary+salary
print(f"Зарплата третьего сотрудника {pay3}")

#задача 3
"""Игра камень ножницы бумага с компьютером
(камень побеждает ножницы / ножницы побеждает бумагу / бумага побеждает камень)
Игрок делает ход и затем компьютер делает ход
Вывести кто победил."""

game_man = input("Камень, ножницы или бумага? ")
import random
game_comp = ["камень", "ножницы", "бумага"]
random.shuffle(game_comp) 
random_game = random.choice(game_comp)
print(f"Компьютер ставит {random_game}")
if game_man == random_game :
    print("Ничья!")
if game_man == "камень" and random_game == "ножницы":
    print("Вы выиграли!")
if game_man == "ножницы" and random_game == "бумага":
    print("Вы выиграли!")
if game_man == "бумага" and random_game == "камень":
    print("Вы выиграли!")
if game_man == "камень" and random_game == "бумага":
    print("Вы проиграли!")
if game_man == "бумага" and random_game == "ножницы":
    print("Вы проиграли!")
if game_man == "ножницы" and random_game == "камень":
    print("Вы проиграли!")

#задача 4
"""Пользователь с клавиатуры вводит количество часов.
Если полученное значение находится в диапазоне 
от 0 до 5 нужно вывести надпись Good Night,
если в диапазоне от 6 до 13 Good Morning,
если в диапазоне от 13 до 17 Good Day, 
если в диапазоне от 17 до 0 Good Evening."""

hour = int(input("Введите количество часов: "))
if 0 <= hour <= 5 : print("Good Night!")
if 6 <= hour < 13 : print("Good Morning!")
if 13 <= hour < 17 :print("Good Day!")
if 17 <= hour < 24 : print("Good Evening!")
