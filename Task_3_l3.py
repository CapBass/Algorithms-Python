"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

def get_array(size=10, min_item=0, max_item=100):
    import random
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array


array = get_array(min_item=-10, max_item=10)

max_value = array[0]
min_value = array[0]
max_idx = 0
min_idx = 0

for idx in range(1, len(array)):
    if array[idx] > max_value:
        max_value = array[idx]
        max_idx = idx
    if array[idx] < min_value:
        min_value = array[idx]
        min_idx = idx

new_array = array.copy()
new_array[max_idx] = min_value
new_array[min_idx] = max_value

print(f'Исходный массив - {array}, \n '
      f'новый массив - {new_array}, \n'
      f'индекс максимального элемента {max_idx} содержит миниальный элемент {min_value}, \n'
      f'индекс минимального элеиента {min_idx} содержит максимальный элемент {max_value} ')
