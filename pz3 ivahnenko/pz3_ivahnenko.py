# # Вариант 9.
# 1. Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно
# из чисел A и B нечетное».
# 2. Арифметические действия над числами пронумерованы следующим образом: 1 —
# сложение, 2 — вычитание, 3 — умножение, 4 — деление. Дан номер действия N
# (целое число в диапазоне 1-4) и вещественные числа A и B (В не равно 0). Выполнить
# над числами указанное действие и вывести результат.


a = int(input('Введите значение A: '))
b = int(input('Введите значение B: '))
result = (a % 2 != 0) or (b % 2 != 0)
print(result)

# ---------------------------------------------------------------------------------------------------------------------------------------------

# a = int(input('Введите значение A: '))
# b = int(input('Введите значение B: '))
# print("1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление.")
# N = int(input('Введите значение от 1 до 4 : '))

# if N == 1:
#     c = (a + b)

# elif N == 2:
#     c = (a - b)

# elif N == 3:
#     c = (a * b)

# elif N == 4:
#     c = (a // b)    

# print ("Результат вычисления: ",c)