# Вариант 9. Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая
# средние температуры по месяцам в году. Преобразовать информацию из строки в
# словарь, с использованием функции найти среднюю и минимальные температуры,
# результаты вывести на экран.


temperature_str = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'

# Разбиваем строку по пробелам
temperature_list = temperature_str.split()

# Извлекаем год
year = temperature_list[0]

temperature_dict = {}

# Добавляем год в словарь
temperature_dict['year'] = year

# список для температур
temperature_values = []

# Проходим по списку температур в строке
for temp_str in temperature_list[1:]:
    # Преобразуем строку в целое число и добавляем в список
    temperature_values.append(int(temp_str))

# Добавляем список температур в словарь
temperature_dict['temperatures'] = temperature_values

# Функция для нахождения средней и минимальной температур
def find_temperatures_stats(temperatures):
    average_temperature = sum(temperatures) / len(temperatures)
    min_temperature = min(temperatures)
    return average_temperature, min_temperature

# Вызываем функцию для нахождения статистики
average_temp, min_temp = find_temperatures_stats(temperature_dict['temperatures'])

# Выводим результаты
print(f'Год: {temperature_dict["year"]}')
print(f'Средняя температура: {average_temp}')
print(f'Минимальная температура: {min_temp}')
