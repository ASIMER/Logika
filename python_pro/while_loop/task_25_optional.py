"""
Сумма последовательности

Пользователь вводит последовательность из любых чисел.
С помощью цикла while и вложенных условий необходимо написать программу,
которая просуммирует отдельно все положительные и все отрицательные числа.

Если пользователь введёт «0»,
программа должна прекратить работу и выдать два результата:
    сумму положительных чисел
    и сумму отрицательных чисел, отдельно друг от друга в столбик.
"""
pos_sum, neg_sum = 0, 0
n = int(input())
while n:
    if n > 0:
        pos_sum += n
    else:
        neg_sum += n
    n = int(input())

print("Сумма положительных чисел =", pos_sum)
print("Сумма отрицательных чисел =", neg_sum)