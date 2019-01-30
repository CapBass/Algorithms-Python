"""Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

import sys
import random


def get_size_var(var):
    size = sys.getsizeof(var)
    if isinstance(var, dict):
        size += sum([get_size_var(v) for v in var.values()])
        size += sum([get_size_var(k) for k in var.keys()])
    elif hasattr(var, '__iter__') and not isinstance(var, (str)):
        size += sum([get_size_var(i) for i in var])
    return size


def max_min_matrix_1(rows, cols):

    matrix = [[random.randint(0, 100) for _ in range(cols)] for _ in range(0, rows)]

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

    return str(f'исходная матрица {matrix} содержит минимальные значения в каждом стобце {min_values} '
               f'максимальное из минимальных значений равно {max_value}'), get_size_var(locals())


def max_min_matrix_2(rows, cols):
    matrix = [[random.randint(0, 100) for _ in range(cols)] for _ in range(0, rows)]
    max_value = 0

    for i in range(0, len(matrix[0])):
        col = []
        for row in matrix:
            col.append(row[i])
        min_value_col = col[0]
        for item in col:
            if item < min_value_col:
                min_value_col = item
        if min_value_col > max_value or max_value == 0:
            max_value = min_value_col

    return str(f'исходная матрица {matrix} среди минимальных значений столбцов матрицы '
               f'содержит максимальное значение {max_value}'), get_size_var(locals())


def max_min_matrix_3(rows, cols):
    matrix = [[random.randint(0, 100) for _ in range(cols)] for _ in range(0, rows)]

    col_mins = []
    for i in range(0, len(matrix[0])):
        col = []
        for row in matrix:
            col.append(row[i])
        col_mins.append(min(col))

    return str(f'исходная матрица {matrix} среди минимальных значений столбцов матрицы {col_mins} '
               f'содержит максимальное значение {max(col_mins)}'), get_size_var(locals())


_, memory_size_1 = max_min_matrix_1(4, 5)
_, memory_size_2 = max_min_matrix_2(4, 5)
_, memory_size_3 = max_min_matrix_3(4, 5)
sizes = [memory_size_1, memory_size_2, memory_size_3]
best = 0
for i,size in enumerate(sizes):
    print(f'объем памяти для реализации алгоритма {i + 1} = {size} байт')
    if size == min(sizes):
        best = i + 1
print(f'лучший алгоритм по затратам памяти это алгоритм под номером {best}')
