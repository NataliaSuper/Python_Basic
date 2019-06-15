# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:

# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import sys
import os
from hw05_easy import *
 
print(sys.argv)
 
answer = ''
while(answer != "q"):
    print("Список возможных действий: ")
    print("[1] - Перейти в папку")
    print("[2] - Просмотреть содержимое текущей папки")
    print("[3] - Удалить папку")
    print("[4] - Создать папку")
    print("Для выхода введите 'q'")
    choise = input("Укажите номер пункта: ")
     
    if choise == 'q':
        break
     
    elif choise == '1':
        dirname = input('Введите имя директории: ')
        file_list = files_in_dir()
        if dirname in file_list:
            os.chdir(dirname)
            print('Перешли в директорию {}'.format(dirname), os.getcwd())
        else:
            print('Такой директории нет.')
     
    elif choise == '2':
        print('Содержимое текущей папки: ')
        main_path = os.getcwd()
        list_dir(main_path)
                
    elif choise == '3':
        dirname = input('Введите имя директории: ')
        if remove_dir(dirname):
            print('{} Директория удалена'.format(dirname))
     
    elif choise == '4':
        dirname = input('Введите имя директории: ')
        if make_dir(dirname):
            print('{} Директория добавлена'.format(dirname))
