"""Задание 1

Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними.
Функция должна вернуть результат вычислений зависящий от третьего аргумент: + сложить их;  -  вычесть; *  умножить; /  разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
"""
def arithmetic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Неизвестная операция"

a = input('Введите a: ')
b = input('Введите b: ')
a=int(a)
b=int(b)
operation = input('Введите операцию над a и b: ')
print(arithmetic(a, b, operation))  # 8

