    # fifth task
def start():
    some_list = [1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 3, 3, 12, 12, 12]

    safe_count = []
    count = 0
    is_set = True

    for item in range(len(some_list)):
        i = some_list[item]
        if i in safe_count:
            continue
        else:
            for numm in range(len(some_list)):

                if some_list[item] == some_list[numm]:
                    count += 1
        if count > 1:
            is_set = False
        safe_count.append(some_list[item])
        print(f"Число {some_list[item]} повторяется {count} раз")
        count = 0
    if not is_set:
        print("Список не состоит польностью из уникальных элементов")
    else:
        print("Все элементы списка уникальны")