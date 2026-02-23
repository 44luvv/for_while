#12th task

numm = input("Введите число: ")
summ = 0

for i in numm:
    if i.isdigit():
        summ += int(i) ** len(numm)
    else:
        continue
if summ == int(numm):
    print(f"{numm} является числом Армстронга")
else:
    print(f"{numm} не является числом Армстронга")