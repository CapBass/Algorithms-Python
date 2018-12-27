""" Сформировать из введенного числа обратное по порядку входящих
в него цифр и вывести на экран. Например,
если введено число 3486, то надо вывести число 6843."""


def reverse(num, n=1, rev_num=''):
    """Функция принимает число, рекурсивно считывает каждую цифру  и
    в обратном порядке конкатенирует цифры как строки, затем вохвращает обратное число"""
    decimal = 10 ** n
    result = num % decimal  # базисное число
    if n != 1:
        sub_num = int(result / 10 ** (n - 1))  # получаем порядковую цифру исходного числа через базисное число
    else:
        sub_num = result
    rev_num += str(sub_num)
    if result == num:  # базовое условие выхода
        return int(rev_num)
    else:
        return reverse(num, n + 1, rev_num)


num = int(input('введите целое число '))
rev_num = reverse(abs(num))
if num < 0:
    rev_num = -rev_num
print(f'Оьратное число {num} это {rev_num}')
