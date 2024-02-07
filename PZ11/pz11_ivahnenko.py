# Вариант 9.
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего максимального элемента:
# Меняем местами первую и последнюю трети:
# 2. Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку фразой введенной
# пользователем.



import random

# # Генерируем последовательность положительных и отрицательных целых чисел
# sequence = [random.randint(-100, 100) for _ in range(20)]

# # Записываем последовательность в текстовый файл
# with open('original_data.txt', 'w') as file:
#     for num in sequence:
#         file.write(str(num) + '\n')

# print('Исходная последовательность сохранена в original_data.txt')

# # Находим индекс последнего максимального элемента
# max_element = max(sequence)
# max_index = len(sequence) - 1 - sequence[::-1].index(max_element)

# # Меняем местами первую и последнюю треть последовательности
# third = len(sequence) // 3
# new_sequence = sequence[2 * third:] + sequence[third:2 * third] + sequence[:third]

# # Записываем обработанную последовательность в новый текстовый файл
# with open('processed_data.txt', 'w') as file:
#     file.write(f'Исходные данные:\n{sequence}\n\n')
#     file.write(f'Количество элементов: {len(sequence)}\n')
#     file.write(f'Индекс последнего максимального элемента: {max_index}\n')
#     file.write(f'Меняем местами первую и последнюю треть:\n{new_sequence}')

# print('Обработанная последовательность сохранена в processed_data.txt')

# ------------------------------------------------------------------2-------------------------------------------------------------------

# Чтение содержимого из файла text18-9.txt и подсчёт количества букв в нижнем регистре
with open('text18-9.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    lowercase_letters_count = sum(1 for char in content if char.islower())

print('Содержимое файла text18-9.txt:')
print(content)
print(f'Количество букв в нижнем регистре: {lowercase_letters_count}')

# Введите последнюю строку для добавления в стихотворную форму
last_line = input('Введите последнюю строку для стихотворения: ')

# Запись текста в стихотворной форме в новый файл poem.txt
with open('poem.txt', 'w', encoding='utf-8') as file:
    # Разбиваем текст на строки
    lines = content.splitlines()

    # Формируем стихотворение, добавляя последнюю строку
    poem_lines = lines[:-1]  # Берём все строки кроме последней
    poem_lines.append(last_line)  # Добавляем введенную пользователем последнюю строку

    # Записываем стихотворение в файл
    file.write('\n'.join(poem_lines))

print('Строки из файла text18-9.txt были оформлены в стихотворной форме в файл poem.txt.')
