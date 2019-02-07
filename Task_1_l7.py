"""Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
 и отсортированный массивы. Сортировка должна быть реализована в виде функции. 
 По возможности доработайте алгоритм (сделайте его умнее)."""
 
import random


def my_bubble_sort(array):
    sort_array = array.copy()
    for i in range(0, len(sort_array) - 1):
        for j in range(i + 1, 0, -1):
            if sort_array[j] > sort_array[j - 1]:
                sort_array[j], sort_array[j - 1] = sort_array[j - 1], sort_array[j]
            else:
                break
    return sort_array


array = [random.randint(-100, 99) for _ in range(0,15)]

print(f'исходный массив - {array} \n отсортированный массив - {my_bubble_sort(array)}')
