numm = int(input("Введите число: "))

count = 0

while numm != 1:
    if numm % 2 == 0:
        numm = numm // 2
        count += 1
    else:
        numm = numm * 3 + 1
        count += 1

print(f"Количество шагов: {count}")