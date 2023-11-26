"""задача
Дана произвольная строка создать строку, в которой 
содержаться только цифры из исходной строки
ПРимер
ввод
АА”АА324А К*К№5 10 79
вывод
32451079"""
import functools
import re
string = "АА”АА324А Кsaser45621 asf  21 124 *К№5 10 79"
string = list(string)
reg_ex = r"\d"
string = list(filter(lambda string1: re.findall(reg_ex, string1), string))
print(''.join(string))

"""задача
Дан список чисел (можно создать любым способом, но приветствуется  лямбду функцию и random).
Необходимо создать новый список чисел, которые будут составлять 70% от исходного числа. 
Для создания такого списка использовать функцию map().
Необходимо посчитать разницу между суммами исходного списка и преобразованного
ПРИМЕР
ввод
100, 50, 30 (сумма 180)
70, 35, 21 (сумма 126)
вывод
54"""
from random import randint
import functools
l1 = []
n = 30
for i in range(n):
    l1.append(randint(0, 100))
l1 = list(filter(lambda x: ((x*0.7)%1 == 0) , l1))
print(f"Первый список чисел: {l1}")
l2 = list(map(lambda x: int(x*0.7), l1))
print(f"Второй список чисел: {l2}")
sum_l1 = functools.reduce(lambda x, y: x+y, l1)
sum_l2 = functools.reduce(lambda x, y: x+y, l2)
print(f"{sum_l1}-{sum_l2}={sum_l1-sum_l2}")
