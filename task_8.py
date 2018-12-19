# Определить, является ли год, который ввел пользователем,
# високосным или невисокосным.

year = int(input('Введите год '))
intercalary = False
if year % 400 == 0:
    intercalary = True
if year % 4 == 0 and year % 100 != 0:
    intercalary = True
if intercalary:
    print(f'Год {year} високосный')
else:
    print(f'Год {year} не високосный')
