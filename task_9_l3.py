"""Найти максимальный элемент среди минимальных элементов столбцов матрицы."""


def get_array(size=10, min_item=0, max_item=100):
    import random
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array


def get_matrix(rows, cols):
    matrix = [get_array(size=cols) for _ in range(0, rows)]
    return matrix


ROWS = 5
COLS = 4
matrix = get_matrix(ROWS, COLS)

matrix_T = []
for i in range(0, len(matrix[0])):
    row = []
    for j in range(0, len(matrix)):
        row.append(matrix[j][i])
    matrix_T.append(row)

min_values = []
for row in matrix_T:
    min_value = row[0]
    for item in row:
        if item < min_value:
            min_value = item
    min_values.append(min_value)

max_value = min_values[0]
for value in min_values:
    if value > max_value:
        max_value = value

print(f'исходная матрица {matrix} содержит минимальные значения в каждом стобце {min_values}, \n'
      f'максимальное из минимальных значений равно {max_value}')
