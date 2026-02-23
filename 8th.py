#8th task

from random import randint

size_matrix = int(input("Введите размерность матрицы: "))

matrix = []

for i in range(size_matrix):
    matrix_two = []
    for j in range(size_matrix):
        matrix_two.append(randint(1, 9))
    matrix.append(matrix_two)

for i in range(size_matrix):
    print(matrix[i])

up = 0
right = size_matrix - 1
summ = 0

for i in range(size_matrix):
    summ += matrix[up][right]
    up += 1
    right -= 1

print(f"Сумма побочной диагонали: {summ}")