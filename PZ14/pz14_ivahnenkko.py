#  В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
# Достоевского (т.е. с различными окончаниями, например, Достоевский,
# Достоевского) в единственном экземпляре.

import re

with open('PZ14/Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

matches = re.findall(r'Достоев\w+', text)

unique_matches = list(set(matches))

for match in unique_matches:
    print(match)

    