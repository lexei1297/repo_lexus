# Ввод первоначального числа
print("Введите число,чтобы узнать количество цифр в нём: ")
number = int(input())
count = 0
# Цикл while для счёта
while number != 0:
    number //= 10
    count = count + 1
print(str(count))
input("\n\nНажмите кнопку Enter чтобы выйти.\n")
