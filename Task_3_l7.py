"""Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда,
 делящий его на две равные части: в одной находятся элементы, которые не меньше
 медианы, в другой – не больше медианы. Задачу можно решить без сортировки
 исходного массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках"""
 
import random
 
def get_median(array):
    median = len(array) // 2 
    for i in array:
        row_idx = 0
        count_item = 0
        for j in array:
            if j < i:
                row_idx += 1
            elif j == i:
                count_item += 1     
        if row_idx == median:
            return i
        for _ in range(1, count_item):
            row_idx += 1
            if row_idx == median:             
                return i
 
 
def get_array(m, start, end):
    array = [random.randint(start, end) for _ in range(0, 2 * m + 1)]
    random.shuffle(array)
    return array


array = get_array(12, -10, 30)
print(f'медиана массива равна {array} равна {get_median(array)}')