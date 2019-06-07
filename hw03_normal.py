# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("Задание 1")

fib1 = fib2 = 1


def fibonacci(n, m):
    a = []
    golden = 1.618034
    for i in range(n, m + 1):
        x = (golden**i- (1 - golden)**i)/(5**(1/2))
        a.append(round(x))
    return a 
 
x = 5
y = 7
 
B = fibonacci(x, y)
 
print(B)
print()

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print("Задание 2")
def sort_to_max(origin_list):
    """
   :param origin_list: seq to be sorted
   :return: sorted seq, ordered by ascending using quicksort
   """
    if len(origin_list) > 1:
        pivot_index = len(origin_list) // 2
        smaller_items = []
        larger_items = []
 
        for i, val in enumerate(origin_list):
            if i != pivot_index:
                if val < origin_list[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)
 
        sort_to_max(smaller_items)
        sort_to_max(larger_items)
        origin_list[:] = smaller_items + [origin_list[pivot_index]] + larger_items
 
    return origin_list
 
 
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print()
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print("Задание 3")

def filter_func(function, iterable):
    return (item for item in iterable if function(item))
 
 
print(list(filter_func(lambda x: True if x % 2 == 0 else False,
                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
print()
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print("Задание 4")

def is_parallelogram(a1, a2, a3, a4):
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and \
       abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False
print(is_parallelogram((1,1), (2,2), (4,2), (4,1)))
