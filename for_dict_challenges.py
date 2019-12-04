from collections import Counter, OrderedDict

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
name = []
for first_name in students:
    name.append(first_name['first_name'])
count_names = Counter(name)
for name, count in count_names.items():
    print(f'{name}: {count}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print()

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
name = []
for first_name in students:
    name.append(first_name['first_name'])
value_names, count_names = Counter(name).most_common(1)[0]
print(f'Самое частое имя среди учеников: {value_names}')

# Пример вывода:
# Самое частое имя среди учеников: Маша
print()
# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

numb_of_class = 0
for classes in school_students:
    numb_of_class += 1
    name_of_class = []
    name_of_class = [name['first_name'] for name in classes]
    value_names, count_names = Counter(name_of_class).most_common(1)[0]
    print(f'Самое частое имя в классе {numb_of_class}: {value_names}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print()

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for sch_class in school:
    male = 0
    female = 0
    for children_name in sch_class['students']:
        if is_male[children_name['first_name']]:
            male += 1
        else:
            female += 1
    numb_of_class = sch_class['class']
    print(f'В классе {numb_of_class} {female} девочки и {male} мальчика')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

print()

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
count_male = {}
count_female = {}
for sch_class in school:
    male = 0
    female = 0
    for children_name in sch_class['students']:
        if is_male[children_name['first_name']]:
            male += 1
        else:
            female += 1
    count_male[sch_class['class']] = male
    count_female[sch_class['class']] = female

print('Больше всего мальчиков в классе {}'.format(max(count_male, key=count_male.get)))
print('Больше всего девочек в классе {}'.format(max(count_female, key=count_female.get)))

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a