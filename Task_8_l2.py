"""Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""


def calc_numeric(num, numeric, numeric_cnt=0, n=1):
    """Функция принимает число, рекурсивно считывает каждую цифру  и
    увеличивает счетчик на единицу, если цифру нужно подсчитывать"""
    decimal = 10 ** n
    result = num % decimal  # базисное число
    if n != 1:
        sub_num = int(result / 10 ** (n - 1))  # получаем порядковую цифру исходного числа через базисное число
    else:
        sub_num = result
    if sub_num == numeric:
        numeric_cnt += 1
    if result == num:  # базовое условие выхода
        return numeric_cnt
    else:
        return calc_numeric(num, numeric, numeric_cnt, n + 1)


num_count = int(input("Укажите количество чисел "))
numeric = int(input("введ1ите цифру, которую нужно посчитать "))
i = 0
result = 0
while i < num_count:
    num = int(input('Введите положительное число '))
    result += calc_numeric(num, numeric)
    i += 1
print(f'Количество цифры {numeric} в заданных числах равно {result}')
