"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. 
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, 
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего."""
from collections import defaultdict as defdict

enterprise_count = int(input('Введите количество предприятий '))

enterprises = defdict(int)
summary = 0.0
QUARTERS = 4

for i in range(enterprise_count):
    enterprise_name = input(f'Введите название {i + 1} предприятия ')
    for quarter in range(QUARTERS):
        profit = int(input(f'Укажите прбыль компании {enterprise_name} за {quarter + 1} квартал '))
        enterprises[enterprise_name] += profit
    summary += enterprises[enterprise_name]

profit_avg_year = summary / enterprise_count


print(f'В этом списке указаны наименований компаний и их годовая прибыль, которая выше средней {profit_avg_year} \n'
      f'{[ (key, value) for key, value in enterprises.items() if value > profit_avg_year]}')
print(f'А в этом списке указаны наименований компаний и их годовая прибыль, которая ниже средней {profit_avg_year} \n'
      f'{[ (key, value) for key, value in enterprises.items() if value < profit_avg_year]}')
