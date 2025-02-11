"""Datetime - импортировать модуль

На текущем времени вывести все нижеперечисленные методы в консоль

Сдать скриншот

datetime.today() - объект datetime из текущей даты и времени. Работает также, как и datetime.now() со значением tz=None.
datetime.fromtimestamp(timestamp) - дата из стандартного представления времени.
datetime.fromordinal(ordinal) - дата из числа, представляющего собой количество дней, прошедших с 01.01.1970.
datetime.now(tz=None) - объект datetime из текущей даты и времени.
datetime.combine(date, time) - объект datetime из комбинации объектов date и time.
datetime.strptime(date_string, format) - преобразует строку в datetime (так же, как и функция strptime из модуля time).
datetime.strftime(format) - см. функцию strftime из модуля time.
datetime.date() - объект даты (с отсечением времени).
datetime.time() - объект времени (с отсечением даты).
datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]) - возвращает новый объект datetime с изменёнными атрибутами.
datetime.timetuple() - возвращает struct_time из datetime.
datetime.toordinal() - количество дней, прошедших с 01.01.1970.
datetime.timestamp() - возвращает время в секундах с начала эпохи.
datetime.weekday() - день недели в виде числа, понедельник - 0, воскресенье - 6.
datetime.isoweekday() - день недели в виде числа, понедельник - 1, воскресенье - 7.
datetime.isocalendar() - кортеж (год в формате ISO, ISO номер недели, ISO день недели).
datetime.isoformat(sep='T') - красивая строка вида "YYYY-MM-DDTHH:MM:SS.mmmmmm" или, если microsecond == 0, "YYYY-MM-DDTHH:MM:SS"
"""
from datetime import datetime, date, time

# Текущее время
now = datetime.now()
print("текущие дата-время1: ", now)
print("текущие дата-время2: ", datetime.today())

# объект datetime из комбинации объектов date и time
new_date = datetime.date(now)
new_time = datetime.time(now)
date_now = datetime.date(now)
time_now = datetime.time(now)
print("объект datetime из комбинации объектов date и time: ", datetime.combine(new_date, new_time))
print("Только дата: ", date_now)
print("Только время: ", time_now)

# timestamp, fromtimestamp
timest = datetime.timestamp(now)
print("Время в секундах с начала эпохи: ", timest)
frtimest = datetime.fromtimestamp(timest)
print("фромтаймштамп: ", frtimest)

import datetime
# fromordinal, toordinal
date1 = datetime.datetime(1970, 1, 1)
ordinal = (now - date1).days
print("ординал: ", ordinal)
fromord = datetime.datetime.fromordinal(ordinal)
print("фромординал: ", fromord)
toOrdinal = date1.toordinal()
print("Количество дней с 01.01.1979: ", toOrdinal)

# возвращает struct_time из datetime
print("datetime.timetuple():", now.timetuple())

# Преобразование datetime в строку
print("Текущие дата-время строкой:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Преобразование строки в datetime
date_string = now.strftime("%Y-%m-%d %H:%M:%S")
format_string = "%Y-%m-%d %H:%M:%S"
print("Дата-время из строки по формату:", datetime.datetime.strptime(date_string, format_string))

# Замена частей datetime
print("Новый объект datetime с изменёнными атрибутами:", now.replace(year=2026, month=11, day=24))

# День недели (понедельник = 0, воскресенье = 6)
print("День недели '0:6':", now.weekday())

# день недели в виде числа, понедельник - 1, воскресенье - 7)
print("День недели '1:7':", now.isoweekday())

# кортеж (год в формате ISO, ISO номер недели, ISO день недели).
print(datetime.datetime.isocalendar(datetime.datetime.now()))

# Форматированная красивая строка вида "YYYY-MM-DDTHH:MM:SS.mmmmmm" или, если microsecond == 0, "YYYY-MM-DDTHH:MM:SS"
print("datetime.isoformat():", now.isoformat(sep='T'))

