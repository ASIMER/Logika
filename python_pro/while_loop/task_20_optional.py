"""
Числа Фибоначчи
Используя цикл while, напиши программу,
которая выводит на экран ряд Фибоначчи до 10-го члена ряда.
"""
a, b = 1, 1
n = 3
print(a, b, sep="\n")
while n <= 10:
    a, b = b, a+b
    print(b)
    n += 1