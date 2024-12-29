# Получаем входные данные
students_class1 = int(input("Введите количество учащихся в первом классе: "))
students_class2 = int(input("Введите количество учащихся во втором классе: "))
students_class3 = int(input("Введите количество учащихся в третьем классе: "))
# Вычисляем количество парт для каждого класса
desks_class1 = (students_class1 + 1) // 2  # Количество парт для 1-го класса
desks_class2 = (students_class2 + 1) // 2  # Количество парт для 2-го класса
desks_class3 = (students_class3 + 1) // 2  # Количество парт для 3-го класса
# Общее количество парт
total_desks = desks_class1 + desks_class2 + desks_class3
# Выводим результат
print("Общее количество парт:", total_desks)