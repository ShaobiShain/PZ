# Создание базового класса "Работник" и его наследование для создания классов
# "Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
# "работать" и "получать зарплату", а классы-наследники будут иметь свои
# уникальные методы и свойства, такие как "управлять командой" и "проектировать
# системы". 

class Worker:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def work(self):
        print("Я работаю")

    def receive_salary(self):
        print("Урааа, я получил зарплату")

class Manager(Worker):
    def manage_a_team(self):
        print("Я управляю командой")

class Engineer(Worker):
    def design_systems(self):
        print("Я проектирую системы")



manager = Manager(name='Петр', position='Менеджер', salary=100000, department='Отдел продаж')
engineer = Engineer(name='Андрей', position='Инженер', salary=80000, specialization='Системный аналитик')


print(manager.attributes)
print(engineer.attributes)

# worker.work()
# worker.receive_salary()
# manager.work()
# manager.receive_salary()
# manager.manage_a_team()
# engineer.work()
# engineer.receive_salary()
# engineer.design_systems()
