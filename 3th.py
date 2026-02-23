# third task

to_num = int(input("Введите до какого числа будет: "))

num_first = 0
num_second = 1
num_third = 0

while num_third <= to_num:
    print(num_third)
    num_third = num_first + num_second
    num_first = num_second
    num_second = num_third

