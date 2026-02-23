#9th task

text = input("Введите строку: ")

vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY")

glasny = 0
soglasny = 0

for i in text:
    if i.isalpha():
        if i in vowels:
            glasny += 1
        else:
            soglasny += 1

print(f"Гласные: {glasny}")
print(f"Согласные: {soglasny}")
print(f"Всего: {glasny + soglasny}")