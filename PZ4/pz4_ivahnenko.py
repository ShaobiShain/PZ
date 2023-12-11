# # # Вариант 9
# # # 1. Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N

# # Получаем от пользователя целое число N
# N = int(input("Введите целое число N (> 0): "))
# if N <=0:
#     ("Введите значение поподающие под условие N (> 0)")
# else:
#     summ = 0.0 # Инициализируем переменную для хранения суммы
#     i = 1

# # Вычисляем сумму 1 + 1/2 + 1/3 + ... + 1/N с помощью цикла while
#     while i <= N:
#         summ = summ + 1/i
#         i += 1


# # Выводим результат
#     print("Сумма равна", summ)

# # # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Дано число A (> 1). Вывести наименьшее из целых чисел K, для которых сумма 1 + 1/2 + ... + 1/K будет больше A, и саму эту сумму.

A = float(input("Введите число A (> 1): "))  # Вводим число A
if A <= 1:
    print("Введите значение поподающие под условие A (> 1)")
else:
    # Инициализируем переменные
    summ = 0.0
    K = 1

    # Пока сумма меньше или равна A, увеличиваем K и добавляем 1/K к сумме
    while summ <= A:
        summ += 1 / K
        K += 1

    # Выводим результат
    print("Наименьшее целое число K:", K - 1)
    print("Сумма 1 + 1/2 + ... + 1/K:", summ)