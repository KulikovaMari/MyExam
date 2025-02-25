"""Задание: Учетная система для транспортных средств
Описание:
Создайте систему учета транспортных средств с использованием следующих концепций ООП: инкапсуляция, абстрактный класс и перегрузка методов. Классы должны позволять хранить данные о транспортных средствах и предоставлять методы для расчета налогов в зависимости от типа транспорта.

Требования:
1	Абстрактный класс Vehicle:
◦	Поля (инкапсуляция): _brand, _model, _year, _price.
◦	Абстрактный метод calculate_tax(), который будет переопределен в наследниках.
◦	Метод vehicle_info(), возвращающий информацию о транспортном средстве.
2	Класс Car (наследник Vehicle):
◦	Реализация метода calculate_tax(): Налог рассчитывается как 10% от цены.
3	Класс Truck (наследник Vehicle):
◦	Перегрузка метода calculate_tax(weight=None):
▪	Если вес не указан, налог = 12% от цены.
▪	Если указан вес, налог увеличивается на 1% за каждые 1000 кг веса.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model, year, price):
        self._brand = brand
        self._model = model
        self._year = year
        self._price = price

    @abstractmethod
    def calculate_tax(self):
        pass

    def vehicle_info(self):
        return f"Brand: {self._brand}, Model: {self._model}, Year: {self._year}, Price: {self._price}"


class Car(Vehicle):
    def calculate_tax(self):
        return self._price * 0.1


class Truck(Vehicle):
    def calculate_tax(self, weight=None):
        tax = self._price * 0.12
        if weight is not None:
            tax += (weight // 1000) * (self._price * 0.01)
        return tax


# Пример
car = Car("Toyota", "Camry", 2020, 20000)
truck = Truck("Volvo", "FH16", 2018, 50000)
print(car.vehicle_info())
print(f"Car Tax: {car.calculate_tax()}")

print(truck.vehicle_info())
print(f"Truck Tax (no weight): {truck.calculate_tax()}")
print(f"Truck Tax (with weight 5000 kg): {truck.calculate_tax(5000)}")
