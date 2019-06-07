# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print("Задание 1. Округление чисел")
def my_round(number, ndigits):
    number=number*(10**ndigits)+0.41
    number = number//1
    return number/(10**ndigits)


print(my_round(2.1234567, 5))
print(my_round(5.4654884, 3))
print(my_round(2.1999967, 3))
print(my_round(4.5678258, 3))
print(my_round(2.9999967, 5))

print()
# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print("Задание 2. Счастливый билет")
import random
 
def lucky_ticket(ticket):
    num = str(ticket)
    if int(num[:1]) + int(num[1:2]) == int(num[-1]) + int(num[-2]):
        return True
    else:
        return False
    
print("Билет 123006 счастливый? ", lucky_ticket(123006))
print("Билет 123006 счастливый? ", lucky_ticket(123006))
print("Билет 123006 счастливый? ", lucky_ticket(12321))
print("Билет 436751 счастливый? ", lucky_ticket(436751))
print()
print("Вариант для случайного числа")    
ticket = random.randint(100000, 999999)
if lucky_ticket is True:
    print("Ваш билет {} счастливый".format(ticket))
else:
    print("Билет {} не выиграл. В следующий раз повезёт!".format(ticket))
