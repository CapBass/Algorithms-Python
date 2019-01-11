""" В одномерном массиве найти сумму элементов, 
	находящихся между минимальным и максимальным элементами. 
	Сами минимальный и максимальный элементы в сумму не включать."""

def get_array(size=10, min_item=0, max_item=100):
    import random
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array


array = get_array()

max_value = array[0]
min_value = array[0]


for idx in range(1, len(array)):
    if array[idx] > max_value:
        max_value = array[idx]
       
    if array[idx] < min_value:
        min_value = array[idx]        
        
summ = 0

for idx,item in enumerate(array):
    if item == max_value or item == min_value:
        for i in range(idx + 1,len(array)):            
            if array[i] == max_value or array[i] == min_value:
                break
            else:
                summ += array[i]
        break

print(f'сумма элементов, находящихся между минимальным элементом {min_value} \n'
      f'и максимальным элементом {max_value} в исходном массиве {array} равна {summ}')
