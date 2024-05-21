# Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
# # любую задачу из ПЗ №№ 2 – 9.

# УСЛОВИЕ ИЗ ПЗ 2 
# Вариант 9; . Даны целые положительные числа A и B (A > B). На отрезке длины A
# размещено максимально возможное количество отрезков длины B (без наложений).
# Используя операцию деления нацело, найти количество отрезков B, размещенных на
# отрезке A


import tkinter as tk

def calculate_segments():
    # получаем данные от пользователя из полей ввода
    A = int(entry_A.get())
    B = int(entry_B.get())

    # выполняем расчет и выводим результат в поле для вывода результата
    if A > B:
        count = A // B
        result_var.set("Количество отрезков В на отрезке А: " + str(count))
    else:
        result_var.set("Введите значение удовлетворяющие условию A>B")

# окно 
root = tk.Tk()
root.title("Расчет отрезков")
root.geometry("300x150")

#поля для ввода данных
entry_A_label = tk.Label(root, text="Введите длину отрезка A:")
entry_A_label.grid(row=0, column=0)
entry_A = tk.Entry(root)
entry_A.grid(row=0, column=1)

entry_B_label = tk.Label(root, text="Введите длину отрезка B:")
entry_B_label.grid(row=1, column=0)
entry_B = tk.Entry(root)
entry_B.grid(row=1, column=1)

# кнопка
calculate_button = tk.Button(root, text="Расчет", command=calculate_segments)
calculate_button.grid(row=2, column=0, columnspan=2)

#вывод
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
