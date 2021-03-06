# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()
print("Задание 1")

fruits = ["яблоко", "банан", "киви", "арбуз"]
for i, item in enumerate(fruits):
    print('{:>40}'.format(i + 1),".",item)

print()
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("Задание 2")

list_1 = [1, 3, 5, 3.45, 'ddd', "s", 333, 9, 'Hello']
list_2 = [2, 1, 8, 9, "s", 5]

print('Первый список: {}'.format(list_1))
print('Второй список: {}'.format(list_2))

for i in list_1[:]:
     for e in list_2[:]:
         if e == i:
            list_1.remove(i)
print('Уникальные значения в списке 1: {}'.format(list_1))

print()

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("Задание 3")
import random
numbers = []
for i in range(20):
    numbers.append(random.randint(1, 1000))
print("Произвольный список: ", numbers)
new_numbers = []
for f in numbers:
    if f % 2 == 0:
     k = f / 4     
    else:
     k = f * 4
    new_numbers.append(k)
print("Сформирован новый список, исходя из условия задачи: если элемент списка 1 кратен 2, то делим его на 4, если нет, то умножаем на 2:")
print(new_numbers)
