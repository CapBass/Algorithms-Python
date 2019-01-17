'''Написать два алгоритма нахождения i-го по счёту простого числа'''


# import cProfile
# python -m timeit -n 100 -s "import task_3" "task_3.fib(10)"


def not_sieve(count):    
    if count == 1:
        return 2
    else:        
        N = count ** 2
        
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
        if len(prime_numbers) == count:
            break
    return prime_numbers[len(prime_numbers) - 1]

	
# timeit
# 100 loops, best of 3: 147 usec per loop - 50
# 100 loops, best of 3: 415 usec per loop - 100
# 100 loops, best of 3: 1.11 msec per loop - 200
# 100 loops, best of 3: 2.99 msec per loop - 400
# 100 loops, best of 3: 7.95 msec per loop - 800

# cProfile
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.011    0.011    0.012    0.012 <ipython-input-32-3eed162a8970>:8(not_sieve) - 1000
#       1    0.126    0.126    0.129    0.129 <ipython-input-32-3eed162a8970>:8(not_sieve) - 5000
#       1    0.291    0.291    0.294    0.294 <ipython-input-32-3eed162a8970>:8(not_sieve) - 10000


def sieve(count):
    if count == 1:
        return 2
    else:        
        N = count ** 2
    
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
        if len(prime_numbers) == count:
            break

    del numeracy
    return prime_numbers[len(prime_numbers) - 1]


# timeit
# 100 loops, best of 3: 783 usec per loop - 50
# 100 loops, best of 3: 3.38 msec per loop - 100
# 100 loops, best of 3: 14.2 msec per loop - 200
# 100 loops, best of 3: 64.9 msec per loop - 400
# 100 loops, best of 3: 313 msec per loopp - 800

# cProfile	
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.442    0.442    0.540    0.540 <ipython-input-32-3eed162a8970>:46(sieve) - 1000
#        1   12.843   12.843   14.480   14.480 <ipython-input-32-3eed162a8970>:46(sieve) - 5000
#        1   54.403   54.403   61.389   61.389 <ipython-input-32-3eed162a8970>:46(sieve) - 10000



'''Вывод: алгоритм исключения делителей имеет асимптотическую сдложность О(1.5N), а решето Эратосфена имеет асимптотическую сложность О(N**2),
следовательно алгоритм поиска i-ого по счету простого числа методом исключения делителей существенно быстрее.'''