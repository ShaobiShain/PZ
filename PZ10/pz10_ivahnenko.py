# Вариант 9.
# {В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
# мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. полный список всех товаров.
# 2. в каких магазинах можно приобрести одновременно молоко и сыр.
# 3. в каких магазинах можно приобрести сахар.

# Заданные множества для каждого магазина
magnit = {'молоко', 'соль', 'сахар'}
pyaterochka = {'мясо', 'молоко', 'сыр'}
perekrestok = {'молоко', 'творог', 'сыр', 'сахар'}

print("-"  * 30 + "Задание 1" + "-"  * 30 )
# 1
# Полный список всех товаров
full_product_list = magnit | pyaterochka | perekrestok
print('Полный список всех товаров:', full_product_list)

print("-"  * 30 + "Задание 2" + "-"  * 30 )
# 2
# Находим пересечение множеств для товаров молока и сыра
common_items = magnit & pyaterochka & perekrestok

# Определяем магазины, в которых есть найденные товары
stores_with_common_items = []

if 'молоко' in common_items:
    stores_with_common_items.append('Магнит')

if 'сыр' in common_items:
    stores_with_common_items.append('Пятерочка')

# Проверяем, есть ли и в перекрестке
if 'молоко' in perekrestok and 'сыр' in perekrestok:
    stores_with_common_items.append('Перекресток')

# Выводим результат
if stores_with_common_items:

    print(f"Молоко и сыр можно приобрести в следующих магазинах: {', '.join(stores_with_common_items)}")
else:
    print("Ни в одном магазине нет одновременно молока и сыра.")

print("-"  * 30 + "Задание 3" + "-"  * 30 )
# 3
# Магазины, где можно приобрести сахар
    
stores_with_sugar = []

# проверка на наличие сахара в магазине:
if "сахар" in magnit:
    stores_with_sugar.append("Магнит")

if "сахар" in pyaterochka:
    stores_with_sugar.append("Пятерочка")

if "сахар" in perekrestok:
    stores_with_sugar.append("Перекресток") 

if stores_with_sugar:
    print(f"сахар можно преобрести в магазине: {', '.join(stores_with_sugar)}")
else:
    print("сахара нет - закончился.")












# if magnit=='молоко':
#     print('magnit')
# elif pyaterochka=='молоко':
#     print('pyaterochka')
# elif perekrestok=='молоко' :
#     print('perekrestok')
