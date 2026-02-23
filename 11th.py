#11th task

numm = int(input("Введите число: "))

some_list = []
summ = 0

for i in range(1, numm):
    if i == numm:
        continue
    else:
        if numm % i == 0:
            some_list.append(i)
        else:
            continue

print(some_list[0], end=" ")
for i in range(1, len(some_list)):
    print(f"+ {some_list[i]}", end=" ")
    summ += some_list[i]
print(f"= {summ + 1}")

if summ + 1 == numm:
    print(f"Число {numm} является совершенным")
else:
    print(f"Число {numm} не являтся свершенным")