"""С помощью питона создать эксель файл
С помощью цикла и модуля рэндом заполнить 2 колонки
Создать второй лист
На втором листе заполнить 3 колонки
1 - дата
2 - порядковый номер в цикле
3 - uuid из модуля uuid"""

import random
import uuid
import datetime
from openpyxl import Workbook

# Создаем новый Excel-файл
wb = Workbook()

# 1. Заполняем первый лист
ws1 = wb.active
ws1.title = "Лист1"
ws1.append(["Число 1", "Число 2"])  # Заголовки колонок

for _ in range(100):  # Генерируем 100 строк случайных чисел
    ws1.append([random.randint(1, 100), random.randint(1, 100)])

# 2. Создаем второй лист и заполняем его
ws2 = wb.create_sheet(title="Лист2")
ws2.append(["Дата", "№", "UUID"])  # Заголовки колонок

for i in range(1, 101):  # Генерируем 100 строк данных
    ws2.append([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i, str(uuid.uuid4())])

# Сохраняем файл
wb.save("DZ_Excel.xlsx")
print("Файл 'DZ_Excel.xlsx' успешно создан!")
