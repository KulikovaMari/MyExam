# Получаем входные данные
n = int(input("Введите кол-во школьников (n): "))
k = int(input("Введите кол-во яблок (k): "))


apples_per_student: int = k // n
apples_left: int  = k % n

print("Каждому школьнику достанется:", apples_per_student)
print("Яблок останется в корзине:", apples_left)

