# Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

idx = int(input('Введите номер буквы в латинском алфавите '))
start_idx = ord('a')
chr_idx = idx - 1 + start_idx
symb = chr(chr_idx)
print(f'Это буква {symb}')
