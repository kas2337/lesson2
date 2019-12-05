import csv

dict_people = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

with open('test.csv', 'w', encoding='utf-8', newline='') as test:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(test, fields, delimiter='\t')
    writer.writeheader()
    for lists in dict_people:
        writer.writerow(lists)


