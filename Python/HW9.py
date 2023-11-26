"""задача
дан  список
запрещено использовать sort, max, count, sum, map
сформировать новый список, с положительными числами"""
from random import randint
nums = []
n = 10
for i in range(n):
    nums.append(randint(-100, 100))
new_nums = []
for index in nums:
    if index > 0: 
        new_nums.append(index) 
print(nums)
print(new_nums)

"""задача
дан  список
запрещено использовать sort, max, count, sum, map
удалить из этого списка, все отрицательные элементы"""
from random import randint
nums = []
n = 10
for i in range(n):
    nums.append(randint(-100, 100))
print(nums)
i = 0
while i < len(nums):
    if nums[i] < 0: 
        del nums[i] 
    else:
        i += 1
print(nums)

"""задача
дан  список
найти  все элементы в этом списке , у которых индекс и значение совпадают.
Исходный список нельзя менять"""
from random import randint
l = []
n = 10
for i in range(n):
    l.append(randint(0, 10))
print(l)
# l = [1, 1, 25, 10, 12, 5, 8, 4, 8]
m = []
a = 0
for i in l:
    if a == i:
        m.append(i)
        a += 1
    else:
        a += 1
if len(m)!=0:
    print(m)
else:
    print("Нет совпадений")
