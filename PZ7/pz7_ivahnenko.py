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
    

N = 10  
symbol1 = 'Hello'  
symbol2 = 'World' 
result_string = alternating_chars(N, symbol1, symbol2)# Вывод чепед. символо
print(result_string)



#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# 2.Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов
# (путь), собственно имя и расширение. Выделить из этой строки имя файла (без
# расширения).


full_file_name = 'hello_world.txt'  
# Разделение имени файла и расширения
file_name, file_extension = full_file_name.split('.')
print("Имя файла без расширения:", file_name)











