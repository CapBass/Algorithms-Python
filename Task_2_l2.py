"""Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""


def calculate(num, n=1, even=0, odd=0):
    """Функция принимает число и рекурсивно считывает каждую цифру на четное или не четное"""
    decimal = 10 ** n
    result = num % decimal  # базисное число
    if n != 1:
        sub_num = int(result / 10 ** (n - 1))  # получаем порядковую цифру исходного числа через базисное число
    else:
        sub_num = result
    if sub_num % 2 == 0:
        even += 1
    else:
        odd += 1
    if result == num:  # базовое условие выхода
        return even, odd
    else:
        return calculate(num, n + 1, even, odd)


num = int(input('введите натуральное число '))
even_cnt, odd_cnt = calculate(num)
print(f'Натуральное число {num} содержит {even_cnt} четных числе и {odd_cnt} нечетных ')
