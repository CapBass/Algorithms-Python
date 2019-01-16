""" В одномерном массиве целых чисел определить два наименьших элемента. 
	Они могут быть как равны между собой (оба являться минимальными), 
	так и различаться."""

def get_array(size=10, min_item=0, max_item=100):
    import random
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array


array = get_array(min_item=-10, max_item=5)


min_value_1 = array[0]
min_value_2 = array[1]

if min_value_1 > min_value_2:
    min_value_1 = array[1]
    min_value_2 = array[0]

for idx in range(2, len(array)):
    if array[idx] < min_value_1:
        min_value_2 = min_value_1
        min_value_1 = array[idx]
    else:
        if array[idx] < min_value_2:
            min_value_2 = array[idx]


print(f'В исходном массиве {array} первое минимальное значение равно {min_value_1}, \n'
      f'второе минимальное значение равно {min_value_2}')
