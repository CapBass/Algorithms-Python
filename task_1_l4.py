'''Определить, какое число в массиве встречается чаще всего.'''


import random
from collections import Counter
# import cProfile


def get_frequency(N):    
    
    array = [random.randint(-5, 10) for _ in range(N)]
        
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
    return freq_num, freq_num_cnt
	
	
# timeit
# 100 loops, best of 3: 159 usec per loop - 100
# 100 loops, best of 3: 1.31 msec per loop - 1000
# 100 loops, best of 3: 13.1 msec per loop - 10000
# 100 loops, best of 3: 66.3 msec per loop - 50000
# 100 loops, best of 3: 132 msec per loop - 100000
# cProfile
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <ipython-input-17-a40a3f419cb7>:6(get_frequency) - 1000
#      1    0.001    0.001    0.027    0.027 <ipython-input-18-3a725f720efe>:6(get_frequency) - 100000
#      1    0.012    0.012    0.249    0.249 <ipython-input-19-92db37c35f9b>:6(get_frequency)-  1000000

def get_frequency_2(N):    
    
    array = [random.randint(-5, 10) for _ in range(N)]
    
    freq_num = 0
    freq_num_cnt = 1

    for control in array:
        freq_count = 0
        for item in array:
            if item == control:
                freq_count += 1
        if freq_count > freq_num_cnt:
            freq_num_cnt = freq_count
            freq_num = control
    
    return freq_num, freq_num_cnt

	
# timeit
# 100 loops, best of 3: 17.2 usec per loop - 10
# 100 loops, best of 3: 427 usec per loop - 100
# 100 loops, best of 3: 10.5 msec per loop - 500
# 100 loops, best of 3: 30.7 msec per loop - 1000
# 100 loops, best of 3: 125 msec per loop - 2000
# cProfile
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.037    0.037    0.039    0.039 <ipython-input-10-a15a22223ff1>:33(get_frequency_2) - 1000
#      1    3.280    3.280    3.303    3.303 <ipython-input-11-c0320bf03c9c>:33(get_frequency_2) - 10000
#      1  336.039  336.039  336.266  336.266 <ipython-input-12-eacbbea6974e>:33(get_frequency_2) - 100000

def get_frequency_3(N):    
    
    array = [random.randint(-5, 10) for _ in range(N)]
    
    counter_dict = Counter(array)
    freq_num = 0
    freq_num_cnt = 1
    for key, value in counter_dict.items():
        if value > freq_num_cnt:
            freq_num_cnt = value
            freq_num = key
    return freq_num, freq_num_cnt


# timeit
# 100 loops, best of 3: 133 usec per loop - 100
# 100 loops, best of 3: 1.29 msec per loop - 1000
# 100 loops, best of 3: 12.6 msec per loop - 10000
# 100 loops, best of 3: 64.3 msec per loop - 50000
# 100 loops, best of 3: 132 msec per loop - 100000
# cProfile
# calls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.003    0.003 <ipython-input-14-ee383f894c04>:58(get_frequency_3) - 1000
#     1    0.000    0.000    0.023    0.023 <ipython-input-15-8b0933997d4e>:58(get_frequency_3) - 10000
#     1    0.000    0.000    0.213    0.213 <ipython-input-16-7dfb1f21af6e>:58(get_frequency_3) - 100000

'''Вывод: первая и третья реализация имеют асимптотическую сложность O(n). Алгоритм, использующий коллекцию
незначительно быстрее аналогичного первого алгоритма без использования коллекции. Вторая реализация имеет
асимптотическую сложность O(N**2), что делает данные алгоритм самым неэффвективным из представленных здесь реализаций.'''
