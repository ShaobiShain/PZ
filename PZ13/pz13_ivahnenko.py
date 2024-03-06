# Вариант 9.
# 1. В матрице элементы второго столбца заменить элементами из одномерного
# динамического массива соответствующей размерности.
# 2. В матрице найти среднее арифметическое положительных элементов, кратных 3.

import numpy as np

# Создаем пример матрицы
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

replacement_column = np.array([10, 11, 12])

# Замена второго столбеца в матрице на значения из replacement_column
matrix[:, 1] = replacement_column

print(matrix)

# --------------------------------------------------------------2--------------------------------------------------------------------------


# def average_positive_multiples_of_3(matrix):
#     # список положительных элементов, кратных 3, с использованием спискового включения
#     multiples_of_3 = [elem for row in matrix for elem in row if elem > 0 and elem % 3 == 0]
    
#     # Вычисляем сумму всех таких элементов
#     total = sum(multiples_of_3)
    
#     # Вычисляем количество элементов в списке
#     count = len(multiples_of_3)
    
#     # Если элементов нет, возвращаем 0, чтобы избежать деления на 0
#     if count == 0:
#         return 0
    
#     # Возвращаем среднее арифметическое положительных элементов, кратных 3
#     return total / count

# # Пример матрицы
# matrix = [
#     [3, -6, 9],
#     [12, 5, 18],
#     [-3, 6, 7]
# ]

# result = average_positive_multiples_of_3(matrix)
# print("Среднее арифметическое положительных элементов, кратных 3, в матрице:", int(result))





