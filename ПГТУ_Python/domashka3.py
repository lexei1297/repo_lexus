#С помощью какой операции можно заменить 
#последний элемент 
#кортежа tpl = (1, 2, 3) на 4
tpl = (1, 2, 3, 4, 5, 6)
list = []
a = 0
for item in tpl:
    Index = item
for a in range(1, Index - 1):
    list.append(a)
    a = a + 1
list.append(Index)
tpl1 = tuple(list)
print(tpl)
print(tpl1)