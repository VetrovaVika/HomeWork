"""ЗАДАЧА
Дано: 3 стороны треугольника
Проверить существует ли треугольник"""

a = int(input("Первая сторона треугольника: "))
b = int(input("Вторая сторона треугольника: "))
c = int(input("Третья сторона треугольника: "))
if a+b>c and a+c>b and b+c>a:
    print("Такой треугольник существует")
else:
    print("Такого треугольника не существует")

"""ЗАДАЧА
Дано:
●	из чего переводим: часов, минут, секунд (что-то одно на выбор пользователя)
●	во что переводим: часов, минут, секунд (что-то одно на выбор пользователя)
●	кол-во переводимых единиц
реализовать интерфейс для перевода из (часов, минут, секунд) в (часов, минут, секунд)"""

conversion1 = int(input("""
Выберете еденицу измерения:
    1 - час
    2 - минута
    3 - секунда
        """))
time1 = int(input("Введите количество едениц: "))
conversion2 = int(input("""
Выберете еденицу измерения, в которую осуществляем перевод:
    1 - час
    2 - минута
    3 - секунда
        """))
if conversion1==1 and conversion2==1: 
    time2=time1 
    print(f"{time1} час = {time2} час")
elif conversion1==1 and conversion2==2: 
    time2=time1*60
    print(f"{time1} час = {time2} минут")
elif conversion1==1 and conversion2==3: 
    time2=time1*3600
    print(f"{time1} час = {time2} секунд")
elif conversion1==2 and conversion2==1: 
    time2=time1/60
    print(f"{time1} минут = {time2} час")
elif conversion1==2 and conversion2==2: 
    time2=time1
    print(f"{time1} минут = {time2} минут")
elif conversion1==2 and conversion2==3: 
    time2=time1*60
    print(f"{time1} минут = {time2} секунд")
elif conversion1==3 and conversion2==1: 
    time2=time1/3600
    print(f"{time1} секунд = {time2} час")
elif conversion1==3 and conversion2==2: 
    time2=time1*60
    print(f"{time1} секунд = {time2} минут")
elif conversion1==3 and conversion2==3: 
    time2=time1
    print(f"{time1} секунд = {time2} секунд")


"""#-------------------------ЗАДАЧА ПОИСК ОШИБОК-----------------------------#
калькулятор
доступны операции умножить и поделить"""
# num1 = 5
# operation = '*' #должен быть выбор операции
# num2 = 6
# if operation == '*': 
#     print(num1/num2) #здесь должно быть умножение
# if operation == '/': #используем elif, т.к. одна и та же операция
#     print(num1/num2)
# else:
#     print("нет такой операции")

#----------------решение--------------------#
num1 = 5
operation = input("Введите операцию * или /: ")
num2 = 6
if operation == '*': 
    print(num1*num2) 
elif operation == '/':
    print(num1/num2)
else:
    print("нет такой операции")

"""#-------------------------ЗАДАЧА-----------------------------#
# Перевод Из мм в м, из м в км (и наоборот)"""

l = int(input("Введите значение для перевода ")) #добавьте проверку на >=0
if l <= 0: 
    print("Введенное значение должно быть больше нуля!")
else:
    start = input("Переводим из mm, m или km? ") #  из которого делается перевод
    print("Одну и ту же еденицу измерения выбирать нельзя!") 
    end = input("Переводим в mm, m или km? ") #  в который делается перевод
    match start:
        case 'm':
            match end:
                case 'mm':
                    print(l*1000) #м в мм
                case 'km':
                    print(l/1000) #м в км
                case _:
                    print("Некорректные данные")
        case 'mm':
            match end:
                case 'm':
                    print(l/1000) #мм в м
                case 'km':
                    print(l/1000000) #мм в км
                case _:
                    print("Некорректные данные")
        case 'km':
            match end:
                case 'm':
                    print(l*1000) #км в м
                case 'mm':
                    print(l*1000000) #км в мм
                case _:
                    print("Некорректные данные")
        case _:
            print("Введите один из предложенных вариантов")
