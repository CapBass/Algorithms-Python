# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

num = int(input('Введите трехзначное число '))
numeral_1 = int(num / 100)
numeral_2 = int((num % 100) / 10)
numeral_3 = (num % 100) % 10
summ = numeral_1 + numeral_2 + numeral_3
product = numeral_1 * numeral_2 * numeral_3
print(f'Сумма цифр {numeral_1}, {numeral_2} и {numeral_3} равна {summ}')
print(f'Произведение чисел {numeral_1}, {numeral_2} и {numeral_3} равно {product}')
