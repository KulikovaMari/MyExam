"""Напишите программу, которая получает от пользователя число n и выводит n строк с результатом умножения чисел от 1 до n на символ *."""
n = int(input("Введите целое число (n): "))
#for 1 to n
 #   print('*'*n\n)
for i in range(1, n + 1):    print(f"{i * '*'}")


