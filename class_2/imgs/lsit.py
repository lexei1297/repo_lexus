list1 = []
list2 = []
while True:
    user_action = input("type write points for list 1, list 2 or find (to find min/max values)")
    user_action = user_action.strip()

    match user_action:
        case 'list1':
          point1 = input("Enter a value for list1: ")
          list1.append(point1)
        case 'list2':
            point2 = input("Enter a value for list1: ")
            list2.append(point2)
        case 'find':
            biglist = []
            biglist.append(zip(list1, list2))
            a = max(biglist)
            b = min(biglist)
            print("Max value for list = ", a)
            print("Min value for list = ", b)
        case 'exit':
            break
print("Bye!")
