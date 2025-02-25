"""Задание:
1	Создайте класс Calculator. В классе реализуйте метод calculate, который будет выполнять различные вычисления в зависимости от входных параметров.
2	Логика метода calculate:
◦	Вариант 1: Если передано два числовых аргумента, метод должен возвращать их сумму.
◦	Вариант 2: Если передано три числовых аргумента, метод должен возвращать их произведение.
◦	Вариант 3: Если передан один аргумент типа list (список чисел), метод должен возвращать сумму элементов списка.
◦	Вариант 4 (дополнительно): Если среди аргументов есть строки, метод должен вернуть конкатенацию строковых представлений всех аргументов.
3	Реализация:
◦	Для реализации «перегрузки» используйте аргументы переменной длины (*args) и внутри метода определяйте логику в зависимости от len(args) и типов элементов.
◦	Обработайте ситуацию, когда аргументы не соответствуют ни одному варианту (выведите сообщение об ошибке или верните None).
4	Тестирование:
◦	Создайте несколько примеров использования метода calculate:
▪	Вычислите сумму для двух чисел.
▪	Вычислите произведение для трех чисел.
▪	Вычислите сумму для списка чисел.
▪	Выведите результат для смешанных аргументов (например, число и строку).
"""
class Calculator:
    def calculate(self, *args):
        if len(args) == 2 and all(isinstance(arg, (int, float)) for arg in args):
            return sum(args)
        elif len(args) == 3 and all(isinstance(arg, (int, float)) for arg in args):
            result = 1
            for arg in args:
                result *= arg
            return result
        elif len(args) == 1 and isinstance(args[0], list) and all(isinstance(num, (int, float)) for num in args[0]):
            return sum(args[0])
        elif any(isinstance(arg, str) for arg in args):
            return ''.join(map(str, args))
        else:
            return None

# Тестирование
calc = Calculator()
print(calc.calculate(2, 3))  # Сумма двух чисел
print(calc.calculate(2, 3, 4))  # Произведение трех чисел
print(calc.calculate([1, 2, 3, 4]))  # Сумма списка чисел
print(calc.calculate(2, "Hello", 8))  # Конкатенация строки и чисел
