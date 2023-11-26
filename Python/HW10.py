"""задача
Найти наиболее часто встречающийся элемент в массиве целых чисел"""
matrix = [1, 2, 4, 4, 3, 2, 2, 4, 2, 2]
a = 0 # повторяющийся элемент
b = 0 # как часто повторяется
for i in matrix:
    max_ = matrix.count(i)
    if b < max_:
        a = i
        b = max_
print(f"Элемент {a} повторяется {b} раз")

"""задача
Поменять местами наибольший и наименьший элементы массива"""
l = [1, 2, 4, 4, 3, 2, 2, 5, 4, 2, 2]
print(l)
max_el = max(l)
min_el = min(l)
a = l.index(max_el)
b = l.index(min_el)
l[a], l[b] = l[b], l[a]
print(f"Наибольший элемент = {max_el}, найименьший элемент = {min_el}")
print(l)

"""задача
напечатать прямоугольник (заданы длина, ширина и символ) при помощи цикла for"""
a = int(input("Введите ширину: "))
b = int(input("Введите высоту: "))
for i in range(b):
    if i == 0 or i == b - 1:
        for j in range(a):
            print('*', end=' ')
    else:
        for j in range(a):
            print('*', end=' ')
    print()

"""задача
напечатать полый прямоугольник (заданы длина, ширина и символ) при помощи цикла for"""
a = int(input("Введите ширину: "))
b = int(input("Введите высоту: "))
for i in range(b):
    if i == 0 or i == b - 1:
        for j in range(a):
            print('*', end=' ')
    else:
        print('*', end=' ')
        for j in range(1, a - 1):
            print(' ', end=' ')
        print('*', end=' ')
    print()
