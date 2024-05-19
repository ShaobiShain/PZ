# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют сохранять информацию из экземпляров класса (3 шт.)
# в файл и загружать ее обратно. Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате.

import pickle
from colorama import init, Fore, Back, Style

init()

print(Style.BRIGHT + Fore.GREEN)
print("+──────────────────────────────────────────────────────── +\n| ╔╗╔══╗╔══╗ ╔══╗╔╗   ╔╗╔══╗╔╗╔╗ ╔══╗╔═══╗╔════╗╔══╗╔═══╗ |\n| ║║║╔═╝║╔╗║ ║╔╗║║║   ║║║╔═╝║║║║ ║╔╗║║╔═╗║╚═╗╔═╝║╔╗║║╔═╗║ |\n| ║╚╝║  ║╚╝║ ║║║║║╚══╗║╚╝║  ║╚╝║ ║║║║║╚═╝║  ║║  ║║║║║╚═╝║ |\n| ║╔╗║  ║╔╗║ ║║║║║╔═╗║║╔╗║  ╚═╗║ ║║║║╚╗╔╗║  ║║  ║║║║║╔══╝ |\n| ║║║╚═╗║║║║╔╝║║║║╚═╝║║║║╚═╗ ╔╝║╔╝║║║ ║║║║  ║║  ║╚╝║║║    |\n| ╚╝╚══╝╚╝╚╝╚═╝╚╝╚═══╝╚╝╚══╝ ╚═╝╚═╝╚╝ ╚╝╚╝  ╚╝  ╚══╝╚╝    | \n+──────────────────────────────────────────────────────── +")

print(Style.BRIGHT + Fore.YELLOW)
print(' '*7 ,"-" * 42)
print(' '*7 ,'| Выберите действие:' , " " * 19 , "|")
print(' '*7 ,"-" * 42)
print(' '*7 ,'| 1. Сложение' , " " * 26 , "|")
print(' '*7 ,"-" * 42)
print(' '*7 ,'| 2. Вычитание' , " " * 25 , "|")
print(' '*7 ,"-" * 42)
print(' '*7 ,'| 3. Умножение'  , " " * 25 , "|")
print(' '*7 ,"-" * 42)
print(' '*7 ,'| 4. Деление'  , " " * 27 , "|")
print(' '*7 ,"-" * 42)
print(' '*7 ,'| 5. Возведение'  , " " * 24, "|")
print(' '*7 ,"-" * 42)
print(' '*7 ,'| 6. Просмотр результата' , " " * 15, "|")
print(' '*7 ,"-" * 42)

math = int(input("        -> "))

class Calculator:
    def __init__(self):
        self.result = None

    def add(self, a, b):
        self.result = a + b
        return self.result

    def sub(self, a, b):
        self.result = a - b
        return self.result

    def mlp(self, a, b):
        self.result = a * b
        return self.result

    def dvd(self, a, b):
        if b == 0:
            raise ValueError("На ноль делить нельзя, УЧИ МАТЕМАТИКУ !!!")
        self.result = a / b
        return self.result

    def sqr(self, a, b):
        self.result = a ** b
        return self.result

calc = Calculator()

if math == 1:
    a = int(input("        A -> "))
    b = int(input("        B -> "))
    result = calc.add(a,b)
elif math == 2:
    a = int(input("        A -> "))
    b = int(input("        B -> "))
    result = calc.sub(a,b)
elif math == 3:
    a = int(input("        A -> "))
    b = int(input("        B -> "))
    result = calc.mlp(a,b)
elif math == 4:
    a = int(input("        A -> "))
    b = int(input("        B -> "))
    result = calc.dvd(a,b)
elif math == 5:
    a = int(input("        A -> "))
    b = int(input("        B -> "))
    result = calc.sqr(a,b)
elif math == 6:
    try:
        loaded_calc = pickle.load(open('calc.pkl', 'rb'))
        result = loaded_calc.result
    except FileNotFoundError:
        print("Нет сохраненного результата.")
else:
    print("Неверный выбор.")

print(Style.BRIGHT + Fore.WHITE)
print("        Результат -> ", result)
print("  ")

# Сохранение результата в файл
pickle.dump(calc, open('calc.pkl', 'wb'))
