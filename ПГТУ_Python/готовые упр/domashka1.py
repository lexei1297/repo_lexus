#Напишите код, который выводит
#на экран отсортированный по возрастанию 
#список квадратов элементов digits
digits = [5, 2, 3, 4, 9, 6]
squares = []
digits.sort()
for digit in digits:
    digit = digit ** 2
    squares.append(digit)
print("\Первый список выглядит так:", digits)
print("\Второй список выглядит так:", squares)