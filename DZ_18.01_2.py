"""Задание 2

Написать функцию is_year_leap, принимающую 1 аргумент — номер года, и возвращающую True, если год високосный, и False иначе."""

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

Year = input("Введите год: ")
Year = int(Year)
print(is_year_leap(Year))

   

