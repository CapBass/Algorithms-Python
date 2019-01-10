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

max_value = 0

for i in range(0, len(matrix[0])):
    col = []
    for row in matrix:
        col.append(row[i])
    # print(col)
    min_value_col = col[0]
    for item in col:
        if item < min_value_col:
            min_value_col = item    
    if min_value_col > max_value or max_value == 0:
        max_value = min_value_col
        
print(f'исходная матрица {matrix} \n среди минимальных значений столбцов матрицы'
      f'содержит максимальное значение {max_value}')
        
