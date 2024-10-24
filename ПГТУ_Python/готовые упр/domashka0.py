#Напишите программу, которая 
#выведет на экран список пар имя 
#номер, записанных в один 
#строковый объект через пробел.
names = ['Петров', 'Сидоров', 'Михайлов', 'Сидоров']
tabs = [123, 124, 125, 126]
output = []
zero = 0
for i in names:
    a = names[zero]
    b = tabs[zero]
    c = f"{a} {b}"
    output.append(c)
    zero = zero + 1
print(output)