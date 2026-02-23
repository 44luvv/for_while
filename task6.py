    # sixth task
def start():
    some_list = [1, 2, 3 , 4, 5, 8, 10]
    some_list = list(set(some_list))
    some_list.sort()
    print(some_list)
    numm = int(input("Введите число которое хотите найти: "))
    left = 0
    right = len(some_list) - 1
    count = 0
    is_true = False

    if some_list[left] == numm:
        is_true = True
        count = left + 1
    elif some_list[right] == numm:
        is_true = True
        count = right + 1
    else:
        while not is_true:
            if some_list[(left + right) // 2] == numm:
                is_true = True
                count = ((left + right) // 2) + 1
            else:
                if some_list[(left + right) // 2] < numm:
                    left = (left + right) // 2
                else:
                    right = (left + right) // 2

    print(f"Ваше число по счету в списке: {count}")