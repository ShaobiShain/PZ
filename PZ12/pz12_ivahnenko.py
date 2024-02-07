# Вариант 9.
# 1.Даны две последовательности. Найти элементы, общие для двух
# последовательностей и их количество.
# 2. Из заданной строки отобразить только символы нижнего регистра. Использовать
# библиотеку string. Строка'In PyCharm, you can specify third-party standalone applications and
# run them as External Tools'

# Даны две последовательности
seq1 = [1, 2, 3, 4, 5]
seq2 = [3, 4, 5, 6, 7]

# Находим общие элементы для двух последовательностей
common_elements = set(seq1) & set(seq2)

# Количество общих элементов
count_common_elements = len(common_elements)

print(f'Общие элементы для двух последовательностей: {common_elements}')
print(f'Количество общих элементов: {count_common_elements}')

# ----------------------------------------------------2------------------------------------------------------

import string

# Заданная строка
input_string = "In PyCharm, you can specify third-party standalone applications and run them as External Tools"

# Получаем все символы нижнего регистра из заданной строки с помощью метода строк
lowercase_chars = ''.join(filter(lambda x: x in string.ascii_lowercase, input_string))

print("Символы нижнего регистра из заданной строки:")
print(lowercase_chars)