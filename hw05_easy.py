# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
import sys

def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(dir_path + ' - такой директории нет')

path_dir =[('dir_' + str(i + 1)) for  i in range(9)]

def make_dir(paths):
    dir_path = os.path.join(os.getcwd(),paths)
    try:
        os.mkdir(dir_path)
        print('Создана директория', path_dir)
    except:
        print(dir_path + ' - такая директория уже есть')
     


# что-то не так, не могу понять что именно
def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        os.rmdir(path_dir)
    except:
        print(path_dir + ' - такой директории нет')
"""for i in path_dir:
    delete_dir(path_dir[i])"""
        
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()
 


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file(first_file,backup_file):
    try:
        shutil.copy(first_file,backup_file)
        print(f'Копия файла {first_file} создана')
    except:
        print('Копирование не удалось')

answer = ''
while(answer != "q"):
    print("Список возможных действий: ")
    print("[1] - создать директории dir_1 - dir_9")
    print("[2] - удалить папки dir_1 - dir_9")
    print("[3] - отобразить папки текущей директории")
    print("[4] - создать копию файла, из которого запущен данный скрипт")
    print("Для выхода введите 'q'")
    choise = input("Укажите номер пункта: ")

    if choise == 'q':
        break

    elif choise == '1':
        print('Мы находимся в директории: ', os.getcwd())
        print("создание директорий dir_1 - dir_9")
        for i in path_dir:
            make_dir(i)

    elif choise == '2':
        pass

    elif choise == '3':
        print('Файлы текущей директории: ')
        list_dir(main_path)

    elif choise == '4':
        print('Создание копии файла, из которого запущен данный скрипт')
        first_file = sys.argv[0]
        backup_file = first_file + '.backup'
        copy_file(first_file,backup_file)

