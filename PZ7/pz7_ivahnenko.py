# Вариант 9
# 1. Дано четное число N (>0) и символы C1 и C2. Вывести строку длины N, которая
# состоит из чередующихся символов C1 и C2, начиная с C1

def alternating_chars(N, C1, C2):
    # Функция принимает три аргумента:
    #  N - длина строки 
    # C1 и C2 - символы между которыми будет чередоваться
    result = ''
    # Создание пустой строки, в которую будут добавляться символы
    for i in range(N):
        # Цикл от 0 до N-1 
        if i % 2 == 0:
            # Если индекс четный, добавляем символ C1
            result += C1
        else:         
            result += C2
    return result
    

N = 9  
symbol1 = 'Hello'  
symbol2 = 'World' 
result_string = alternating_chars(N, symbol1, symbol2)# Вывод черед. символов
print(result_string)



#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# 2.Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов
# (путь), собственно имя и расширение. Выделить из этой строки имя файла (без
# расширения).


# способ 1
    
# full_file_name = 'C:\\Users\\Анатолий\\Desktop\\clone_pract\\PZ\\PZ7\\hello_world.txt'

# # Получение имени файла без расширения
# file_extension = full_file_name.split('\\')[-1]
# file_name = file_extension.split('.')[0]

# print("Имя файла без расширения:", file_name)

# способ 2

import os
full_file_name = r'C:\Users\Анатолий\Desktop\clone_pract\PZ\PZ7\hello_world.txt'
# Получение имени файла без расширения
file_name = os.path.splitext(os.path.basename(full_file_name))[0]
print("Имя файла без расширения:", file_name)






