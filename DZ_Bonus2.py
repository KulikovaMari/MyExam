"""Напишите программу, которая получает от пользователя строку целых чисел, и выводит:
•	Количество положительных чисел.
•	Произведение всех отрицательных чисел.
•	Минимальное и максимальное числа без использования функций min() и max().
"""

# Объявляем переменные
list_numbers = []
pos_num_count = 0
neg_num_count = 0
neg_num_prod_count = 0
max_num = 0
min_num = 0

for i in range(10):
    i_str = input('Введите любое целое положительное или отрицательное число: ')
    list_numbers.append(int(i_str))

print('Введённые числа:', list_numbers)

# Обрабатываем список чисел и выводим кол-во положит.,кол-во отриц. и произведение всех отрицательных чисел:
for num in list_numbers:
    if num >= 0:
        pos_num_count += 1
    else:
        neg_num_count += 1
        neg_num_prod_count *= num
print('Кол-во положительных:', pos_num_count)
print('Кол-во отрицательных:', neg_num_count)
print('Произведение всех отрицательных:', neg_num_prod_count)

# Обрабатываем список чисел и выводим max и min числа:
for num in list_numbers:
    if max_num < num:
        max_num = num
print('max число :', max_num)
for num in list_numbers:
    if min_num > num:
        min_num = num
print('min число:', min_num)


