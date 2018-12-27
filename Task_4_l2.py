"""Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры."""

n = int(input('введите количество элементов ряда '))
i = 1
summ = 1
row = 1
while i < n:
    row *= 0.5
    if i % 2 == 0:
        summ += row
    else:
        summ -= row
    i += 1
print(f'cумма {n} элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... равна {summ}')
