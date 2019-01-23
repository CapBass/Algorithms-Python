"""Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, 
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] 
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""
from collections import deque


def num_from_hex(num, mode='to_num'):
    '''Конвератция из шестнадцатиричной с/ч и обратно'''
    hex_values = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    if mode == 'to_num':
        if num in hex_values:
            return hex_values[num]
    elif mode == 'to_hex':
        if num in hex_values.values():
            for key, value in hex_values.items():
                if num == value:
                    return key
    return int(num)


def hex_sum(a, b):
    """Добавляем разряды 0 для одинаковой размерности"""
    if len(a) > len(b):
        for i in range(len(a) - len(b)):
            b.appendleft(0)
    else:
        for i in range(len(b) - len(a)):
            a.appendleft(0)
    """Сам алгоритм суммирования в столбик"""
    result = result = deque()
    digit_cnt = 0
    for i in range(1, len(a) + 1):
        first = num_from_hex(a[len(a) - i])
        second = num_from_hex(b[len(b) - i])
        summary = first + second + digit_cnt
        if summary >= 16:
            remainder = summary % 16
            digit_cnt = 1
        else:
            remainder = summary
            digit_cnt = 0
        result.appendleft(remainder)
    if digit_cnt > 0:
        result.appendleft(digit_cnt)
    result = [str(num_from_hex(i, 'to_hex')) for i in result]

    return result


def hex_multiply(a, b):

    main_multiply = deque()
    result = []

    for i in range(1, len(b) + 1):
        first = num_from_hex(b[len(b) - i])
        digit_cnt = 0
        for j in range(1, len(a) + 1):
            second = num_from_hex(a[len(a) - j])
            multiply = first * second + digit_cnt
            if multiply >= 16:
                remainder = multiply % 16
                digit_cnt = multiply // 16
            else:
                remainder = multiply
                digit_cnt = 0
            main_multiply.appendleft(remainder)
        if digit_cnt > 0:
            main_multiply.appendleft(digit_cnt)
        result.append(main_multiply)
        main_multiply = deque()

    mult_summary = result[0]
    if len(result) > 1:
        for i in range(1, len(result)):
            for j in range(i):
                result[i].append(0)
            mult_summary = deque(hex_sum(mult_summary, result[i]))
    else:
        mult_summary = [str(num_from_hex(i, 'to_hex')) for i in mult_summary]

    return list(mult_summary)

a1 = list(input('Введите первое шестнадцатиричное число '))
operation = input('Введите операцию ')
a2 = list(input('Введите второе шестнадцатиричное число '))
if operation == '+':
    a = deque(a1)
    b = deque(a2)
    result = hex_sum(a, b)
elif operation == '*':
    a = deque(a1)
    b = deque(a2)
    result = hex_multiply(a1, a2)
else:
    result = 'Ошибка'
print(f'результат {operation} над числами {a1} и {a2} равен {result}')
