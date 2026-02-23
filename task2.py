# second task
def start():
    price = int(input("Введите цену товара: "))
    money = int(input("Введите сколько денег она будет откладывать:"))

    pay = 0
    day = 0

    while pay < price:
        for i in range(1, 8):
            if i == 6:
                day += 1
                continue
            else:
                pay += money
                day += 1
            if pay >= price:
                break

    print(f"Вы накопите деньги на телефон суммой {price} через {day} дней!")

