'''
# Задание 4:
Напишите программу, которая запрашивает у пользователя шесть вещественных чисел. 
На экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой. 
Выполните задание без использования встроенных функций min() и max().
'''
list = []
for sum in range(6):
    sum = float(input())
    list.append(sum)
    list.sort()
print(list)
print(list [0])
print(list [-1])