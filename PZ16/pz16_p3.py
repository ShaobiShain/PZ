# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют сохранять информацию из экземпляров класса (3 шт.)
# в файл и загружать ее обратно. Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате.
import pickle
from colorama import init, Fore, Back, Style

init()

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

def save_def(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)

def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# экземпляры
calc1 = Calculator()
calc2 = Calculator()
calc3 = Calculator()
# вызыв. методы
calc1.add(5, 3)
calc2.sub(500, 42)
calc3.mlp(23, 3)
calc3.dvd(102, 3)
# сохр расчеты
save_def(calc1, 'calc1.pkl')
save_def(calc2, 'calc2.pkl')
save_def(calc3, 'calc3.pkl')
# выщружаем из файла
loaded_calc1 = load_def('calc1.pkl')
loaded_calc2 = load_def('calc2.pkl')
loaded_calc3 = load_def('calc3.pkl')
#выводим
print("Результат первого расчета:", loaded_calc1.result)
print("Результат второго расчета:", loaded_calc2.result)
print("Результат третьего расчета:", loaded_calc3.result)
