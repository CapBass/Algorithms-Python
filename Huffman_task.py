"""Закодируйте любую строку из трех слов по алгоритму Хаффмана"""

from collections import Counter, deque

text = 'Это строка для теста'


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Huffman_table:
    def __init__(self, text):
        self.text = text

    def __get_value(self, obj):
        """получаем вес элемента tuple или object"""
        if isinstance(obj, tuple):
            value = obj[1]
        else:
            value = obj.value
        return value

    def __create_tree(self, value, left, right):
        """строим узел бинарного дерева с элементами tuple или object"""
        if isinstance(left, tuple) and isinstance(right, tuple):
            return Node(value, Node(left[0]), Node(right[0]))
        elif not isinstance(left, tuple) and isinstance(right, tuple):
            return Node(value, Node(left.value, left.left, left.right), Node(right[0]))
        elif isinstance(left, tuple) and not isinstance(right, tuple):
            return Node(value, Node(left[0]), Node(right.value, right.left, right.right))
        else:
            return Node(value, Node(left.value, left.left, left.right),
                        Node(right.value, right.left, right.right))

    def __get_huffman_tree(self, frequency):
        """Строим бинарное дерево Хаффмана"""
        tree = None
        max_freq = frequency[len(frequency) - 1][1]

        while len(frequency) > 1:
            left = frequency.popleft()
            right = frequency.popleft()
            value = self.__get_value(left) + self.__get_value(right)
            tree = self.__create_tree(value, left, right)
            if (value < max_freq):
                frequency.rotate(max_freq - value)
                frequency.append(tree)
                frequency.rotate(-(max_freq - value))
            else:
                frequency.append(tree)
        return tree

    def __get_huffman_table(self, bin_tree, path='', huffman_table={}):
        """Получаем закодированную таблицу Хаффмана"""
        if isinstance(bin_tree.value, str):
            huffman_table[bin_tree.value] = path
            return bin_tree.value, path
        self.__get_huffman_table(bin_tree.left, path=f'{path}0', huffman_table=huffman_table)
        self.__get_huffman_table(bin_tree.right, path=f'{path}1', huffman_table=huffman_table)
        return huffman_table

    def encode(self):
        frequency = deque(Counter(self.text).most_common())
        frequency.reverse()
        huffman_tree = self.__get_huffman_tree(frequency)
        huffman_table = self.__get_huffman_table(huffman_tree)
        encoding = []
        for i in self.text:
            if i in huffman_table:
                encoding.append(huffman_table[i])
        return huffman_table, "".join(encoding)


huffman_table, encoding = Huffman_table(text).encode()

print(
    f'Искомый текст "{text}" после кодирования алгоритмом Хаффмана:'
	f'\n{encoding}\nТаблица Хаффмана:{huffman_table}')