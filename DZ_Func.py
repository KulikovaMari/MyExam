"""Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата."""
import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return (perimeter, area, diagonal)

# Input length of square side
#side_length = 5
input_side_length = input('Input length of square side: ')
side_length = int(input_side_length)
result = square(side_length)
print('perimeter, area, diagonal: ')
print(result)
