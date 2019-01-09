"""Определить, какое число в массиве встречается чаще всего."""

def get_array(size=10000, min_item=0, max_item=100):
    import random
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array


array = get_array(size=15, min_item=-5, max_item=5)

freq_num = 0
freq_num_cnt = 1
freq_dict = {}

for item in array:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1

for key in freq_dict.keys():
    if freq_dict[key] > freq_num_cnt:
        freq_num_cnt = freq_dict[key]
        freq_num = key

print(f'в исходном массиве {array} наиболее частый эемент  {freq_num} с частотой {freq_num_cnt}')
