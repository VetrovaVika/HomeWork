#задача 1
"""Дано: температура в цельсиях(число) и давление в паскалях (число).
Написать замерзнет вода или нет.
Вода замерзает при выполнения двух условий:
	1. давление в 10^5 Паскаль
	2. температура меньше либо равно 0 градусов по цельсию"""

temp = int(input("t = "))
pa = int(input("p = "))
if temp <= 0 and pa == 100000 :
    print ("Вода замерзнет")
else:
    print("Вода не замерзнет")

#задача 2
"""Начальник составляет график смены, кто работает а кто нет, он вправе выбрать кого-то 
одного из рабочих или сразу двоих, используя два параметра employee1 и employee2.
В каждый параметр он может написать “работает” или “не работает” (только эти варианты)
Напишите программу, которая в зависимости от выбора начальника выводит информацию  
о количестве работников на смене"""

employee1 = input("Сегодня Петров работает? ")
employee2 = input("Сегодня Иванов работает? ")
work = 0
if employee1 == "работает" and employee2 == "работает":
    work = 2
elif employee1 == "работает" or employee2 == "работает":
    work = 1
print(f"Сегодня в смене {work} сотрудник(а)")

#задача 3
"""Дано два числа. Найдите наибольшее четное число среди них. 
Если оно не существует, выведите фразу "not found"""

num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
if num1 % 2 == 0 and num2 % 2 == 0 :
    if num1 < num2 : print(f"наибольшее четное число {num2}")
    if num1 > num2 : print(f"наибольшее четное число {num1}")
if num1 % 2 != 0 and num2 % 2 == 0:
    print(f"наибольшее четное число {num2}")
if num1 % 2 == 0 and num2 % 2 != 0:
    print(f"наибольшее четное число {num1}")
if num1 % 2 == 0 and num2 % 2 == 0 and num1 == num2 : 
    print("Числа равны и оба четны")    
if num1 % 2 != 0 and num2 % 2 != 0 : print("not found")
