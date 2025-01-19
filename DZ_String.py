"""Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на B, и B, соответственно, на A. Замену можно производить ТОЛЬКО используя функцию replace(). В результате применения функции к исходной строке, функция должна вернуть строку: BBABAABBAAABA
Использовать циклы и оператор IF запрещено."""

def swap_letters(s):
    s = s.replace('A', '*')  # Заменим все 'A' на временный символ '*'
    s = s.replace('B', 'A')  # Заменим все 'B' на 'A'
    s = s.replace('*', 'B')  # Заменим все '*' на 'B'
    return s

# Строка
#string = "AABABBAABBBAB"

string = input('Input only A&B: ')
result = swap_letters(string)
print(result)
