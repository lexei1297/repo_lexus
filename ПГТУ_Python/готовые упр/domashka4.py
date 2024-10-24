#С помощью функции .split()
#получите список из строки
#'hello kitty' и возьмите два
#последних элемента. В качестве
#ответа введите результат вывода.
full_word = 'hello kitty'
str_list = full_word.split()
for word in str_list:
    print(word[-2:])