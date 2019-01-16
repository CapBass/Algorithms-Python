'''Написать два алгоритма нахождения i-го по счёту простого числа'''


# impoert cProfile
# python -m timeit -n 100 -s "import task_3" "task_3.fib(10)"


def not_sieve(N):
    prime_numbers = [2]
    for i in range(3, N + 1, 2): # все нечетные
        if i > 10 and i % 5 == 0: # проверка что число не делится на 5
            continue
        for num in prime_numbers: # проверка на делитель
            if num**2 - 1 > i:
                prime_numbers.append(i)
                break
            if i % num == 0:
                break
        else:
            prime_numbers.append(i)    
    return len(prime_numbers)

	
# timeit
# 100 loops, best of 3: 121 usec per loop - 199
# 100 loops, best of 3: 14.4 msec per loop - 10249
# 100 loops, best of 3: 34.1 msec per loop - 20483
# 100 loops, best of 3: 81 msec per loop - 40849
# 100 loops, best of 3: 252 msec per loop - 100523

# cProfile
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.018    0.018    0.018    0.018 <ipython-input-130-7f4218183894>:2(not_sieve) - 10249
#       1    0.054    0.054    0.054    0.054 <ipython-input-130-7f4218183894>:2(not_sieve) - 20483
#       1    0.101    0.101    0.101    0.101 <ipython-input-130-7f4218183894>:2(not_sieve) - 40849
#       1    0.275    0.275    0.276    0.276 <ipython-input-130-7f4218183894>:2(not_sieve) - 100523

def sieve(N):
    numeracy = [i for i in range(N + 1)]   
    
    numeracy[1] = 0
    
    m = 2
    while m < N:
        if numeracy[m] != 0:
            j = m * 2
            while j < N:
                numeracy[j] = 0
                j = j + m
        m += 1
        
    prime_numbers = []
    for i in numeracy:
        if numeracy[i] != 0:
            prime_numbers.append(numeracy[i])

    del numeracy
    return len(prime_numbers)


# timeit
# 100 loops, best of 3: 58.8 usec per loop - 199
# 100 loops, best of 3: 3.76 msec per loop - 10249
# 100 loops, best of 3: 7.78 msec per loop - 20483
# 100 loops, best of 3: 16.1 msec per loop - 40849
# 100 loops, best of 3: 43.1 msec per loop - 100523

# cProfile	
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.006    0.006    0.007    0.007 <ipython-input-125-6e43b0dd8d33>:1(sieve) - 10249
#        1    0.010    0.010    0.011    0.011 <ipython-input-125-6e43b0dd8d33>:1(sieve) - 20483
#        1    0.021    0.021    0.023    0.023 <ipython-input-125-6e43b0dd8d33>:1(sieve) - 40849
#        1    0.067    0.067    0.073    0.073 <ipython-input-125-6e43b0dd8d33>:1(sieve) - 100523


'''Вывод: алгоритм поиска делителей и решето Эратосфена имеют одинаковую асимптотическую сложность О(n),
но алгоритм решето эратосвена показывает на отметках примерно 3х кратную производительность по сравнению 
с алгоритма поиска делителей, следовательно в данной реализации решето Эратосфена лучше.'''