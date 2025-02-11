"""Создать класс, описывающий группу студентов - `Group`.
Данный класс хранит студентов в виде списка объектов `Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`, `grades`),
а так же необходимый набор методов экземпляра для работы с этими экземплярами."""

class Student:
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

# Добавляем оценки студенту
    def add_grade(self, grade):
        self.grades.append(grade)

# Вычисляем средний балл студента
    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

# Параметры студента
    def __str__(self):
        return f"Студент: {self.name}, Возраст: {self.age}, Средний балл: {self.get_average_grade():.2f}"


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

 #Добавляем студента в группу
    def add_student(self, student):
        self.students.append(student)

# Находим студента с наибольшим средним баллом
    def get_best_student(self):
        return max(self.students, key=lambda student: student.get_average_grade(), default=None)

# Группа студентов
    def __str__(self):
        student_list = "\n".join(str(student) for student in self.students)
        return f"Группа: {self.group_name}\n{student_list}"


# Пример использования
s1 = Student("Алексей", 20, [90, 85, 88])
s2 = Student("Мария", 19, [92, 78, 85])
s3 = Student("Вячеслав", 21, [85, 80, 82])

group = Group("Группа A")
group.add_student(s1)
group.add_student(s2)
group.add_student(s3)

# Вывод списка студентов
print(group)

# Вывод лучшего студента
best_student = group.get_best_student()
print(f"\nЛучший студент: {best_student}")
