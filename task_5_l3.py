"""В массиве найти максимальный отрицательный элемент.
   Вывести на экран его значение и позицию в массиве."""

def get_array(size=10, min_item=0, max_item=100):
    import random
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array


array = get_array(min_item=-11, max_item=10)
max_negative = 0
max_negative_idx = 0
for idx, item in enumerate(array):
    if item < 0:
        if item > max_negative or max_negative == 0:
            max_negative = item
            max_negative_idx = idx
if max_negative < 0:
    print(f'в исходном массиве {array} максимальное отрицательное число {max_negative},\n'
          f'которое находится на позиции {max_negative_idx}')
else:
    print(f'отрицательных чисел в массиве {array} нет')
