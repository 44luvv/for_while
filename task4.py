    # fourth task
def start():
    some_list = [1, 2, 3, -4, 5, -6, 8]

    summ = 0

    for item in range(len(some_list)):
        summ += some_list[item]
    print(f"Сумма всех элементов: {summ}")

    max_element = some_list[0]

    for item in range(len(some_list)):
        if some_list[item] > max_element:
            max_element = some_list[item]
    print(f"Самый большой элемент: {max_element}")

    min_element = some_list[0]
    for item in range(len(some_list)):
        if some_list[item] < min_element:
            min_element = some_list[item]
    print(f"Самый минимальный элемент: {min_element}")