import task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13

is_run = True

while is_run:
    print("2 - Task 2: Маша копит на телефон")
    print("3 - Task 3: Числы Фибоначчи")
    print("4 - Task 4: Сумма чисел, max и min")
    print("5 - Task 5: Уникальные ли числа")
    print("6 - Task 6: Бинарный поиск")
    print("7 - Task 7: Бинарный поиск")
    print("8 - Task 8: Сумма элементов побочной диагонали")
    print("9 - Task 9: Количество согласных и гласных")
    print("10 - Task 10: Простое ли число")
    print("11 - Task 11: Совершенное ли число")
    print("12 - Task 12: Число Армстронга")
    print("13 - Task 13: Кол-во шагов до 1")
    print("0 - Выход")

    numm = int(input("Введите номер пункта: "))
    if numm == 0:
        is_run = False
    elif numm == 2:
        task2.start()
    elif numm == 3:
        task3.start()
    elif numm == 4:
        task4.start()
    elif numm == 5:
        task5.start()
    elif numm == 6:
        task6.start()
    elif numm == 7:
        task7.start()
    elif numm == 8:
        task8.start()
    elif numm == 9:
        task9.start()
    elif numm == 10:
        task10.start()
    elif numm == 11:
        task11.start()
    elif numm == 12:
        task12.start()
    elif numm == 13:
        task13.start()





