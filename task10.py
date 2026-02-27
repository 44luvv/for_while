    #10th task
def start():
    is_simple = False
    numm = int(input("Введите число: "))
    count = 0

    for i in range(1, numm + 1):
        if numm < 0:
            break
        else:
            if numm % i == 0:
                count += 1
            else:
                continue
            if count > 2:
                is_simple = True
                break
    if numm == 0:
        print("0 не являеться ни тем ни тем")
    elif count == 0:
        print("Это отричательное число")
    elif count == 1:
        print("1 не является ни тем ни тем")
    elif is_simple:
        print("Число не простое")
    else:
        print("Число простое")