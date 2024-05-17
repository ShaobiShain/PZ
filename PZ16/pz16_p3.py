# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle

class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

def save_def(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)

def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


obj1 = MyClass(1, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
obj2 = MyClass(2, 'Sed euismod, nisl vitae tincidunt lacinia, nisi nisi ullamcorper nisi, in aliquet massa nisl eget metus.')
obj3 = MyClass(3, 'Proin euismod, augue nec aliquet malesuada, nisl velit egestas velit, eget euismod libero odio vitae lectus')


save_def(obj1, 'obj1.pkl')
save_def(obj2, 'obj2.pkl')
save_def(obj3, 'obj3.pkl')

loaded_obj1 = load_def('obj1.pkl')
loaded_obj2 = load_def('obj2.pkl')
loaded_obj3 = load_def('obj3.pkl')


print(loaded_obj1.attribute1, loaded_obj1.attribute2)
print(loaded_obj2.attribute1, loaded_obj2.attribute2)
print(loaded_obj3.attribute1, loaded_obj3.attribute2)
