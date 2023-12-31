 # 1. Составить программу, в которой функция генерирует четырехзначное число и
# определяет, есть ли в числе одинаковые цифры.

# import random
# # Генерация случайного четырехзначного числа
# def calculation():
#     random_number = random.randint(1000, 9999)
#     print("Сгенерированное число:", random_number)

#     # Проверка на наличие одинаковых цифр
#     if len(set(str(random_number))) != 4:   #Преобразует число random_number в строку,Преобразуем строку цифр в множество (set), убирая повторяющиеся цифры, вычисляет длину этого множества len 
#         print("В числе есть одинаковые цифры.")
#     else:
#         print("В числе нет одинаковых цифр.")
# calculation()

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# 2. Описать функцию Swap(X, Y), меняющую содержимое переменных X и Y (X и Y —
# вещественные параметры, являющиеся одновременно входными и выходными). С
# ее помощью для данных переменных A, B, C, D последовательно поменять
# содержимое следующих пар: A и B, C и D, B и C и вывести новые значения A, B, C,
# D.

def Swap(X, Y):
    return Y, X

# Пример использования функции Swap для переменных A, B, C, D
A,B,C,D = (10,20,30,40)

A, B = Swap(A, B)  # Меняем содержимое переменных A и B
C, D = Swap(C, D)  # Меняем содержимое переменных C и D
B, C = Swap(B, C)  # Меняем содержимое переменных B и C

# Вывод новых значений переменных
print("Новые значения переменных A, B, C, D после замены:")
print(f"A = {A}\nB = {B}\nC = {C}\nD = {D}")