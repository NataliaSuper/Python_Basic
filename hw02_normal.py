# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
import random

numbers = []
for i in range(30):
    numbers.append(random.randint(-100, 100))
print("Произвольный список: ", numbers)
new_numbers = []
for i in numbers:
    if i > 0 and math.sqrt(i) % 1 == 0:
        new_numbers.append(int(math.sqrt(i)))
print("Согласно условиям задачи, создан новый список, состоящий из квадратных корней элементов исходного списка, не имеющие десятичной части:")
print(new_numbers)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print()
print("Задание 2")

dict_day = {
'01': 'первое',
'02': 'второе',
'03': 'третье',
'04': 'четвёртое',
'05': 'пятое',
'06': 'шестое',
'07': 'седьмое',
'08': 'восьмое',
'09': 'девятое',
'10': 'десятое',
'11': 'одиннадцатое',
'12': 'двенадцатое',
'13': 'тринадцатое',
'14': 'четырнадцатое',
'15': 'пятнадцатое',
'16': 'шестнадцатое',
'17': 'семнадцатое',
'18': 'восемнадцатое',
'19': 'девятнадцатое',
'20': 'двадцатое',
'21': 'двадцать первое',
'22': 'двадцать второе',
'23': 'двадцать третье',
'24': 'двадцать четвёртое',
'25': 'двадцать пятое',
'26': 'двадцать шестое',
'27': 'двадцать седьмое',
'28': 'двадцать восьмое',
'29': 'двадцать девятое',
'30': 'тридцатое',
'31': 'тридцать первое',
    }

dict_month = {
'01': 'января',
'02': 'феврал',
'03': 'марта',
'04': 'апреля',
'05': 'мая',
'06': 'июня',
'07': 'июля',
'08': 'августа',
'09': 'сентября',
'10': 'октября',
'11': 'ноября',
'12': 'декабря',
    }
date = '01.01.2000'
date_split = date.split('.')
print(date)
print('{} {} {} года'.format(dict_day[date_split[0]], dict_month[date_split[1]], date_split[2]))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random




# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print()
print("Задание 4")
import math
import random
numbers = []
for i in range(20):
    numbers.append(random.randint(-100, 100))
print("Произвольный список: {}".format(numbers))
unic = set(numbers)
print("Создан список неповторяющихся элементов: {}".format(unic))

unic_numbers = []
for i in numbers:
    if numbers.count(i) == 1:
        unic_numbers.append(i)
print("Элементы исходного списка, не имеющие повторений: {}".format(unic_numbers))
