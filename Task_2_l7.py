"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50).
 Выведите на экран исходный и отсортированный массивы."""

import random


def merge(part_1, part_2):
    result = []
    while len(part_1) > 0 and len(part_2) > 0:
        if part_1[0] > part_2[0]:
            result.append(part_2.pop(0))      
        else:
            result.append(part_1.pop(0))       
    return result + part_1 + part_2


def merge_sort(array):
    if len(array) <= 1:        
        return array
    else:
        decompose = len(array) // 2
        part_1 = merge_sort(array[:decompose])
        part_2 = merge_sort(array[decompose:])
        result = merge(part_1, part_2)
        return result

array = [random.uniform(0, 49) for _ in range(0,15)]
random.shuffle(array)
sort_array = array.copy()

print(f'исходный массив - {array} \n отсортированный массив - {merge_sort(array)}')
