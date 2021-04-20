"""
Используя цикл while и вложенные условия, необходимо написать программу,
которая выведет все числа от нуля до введённого в столбик.
Необходимо учитывать, что пользователь может ввести как положительное,
так и отрицательное число. Если пользователь введет 0, программа должна
вывести 0.
"""
max_n = int(input())
n, sign = 0, -1 if max_n < 0 else 1
print(n)
while n+1 < abs(max_n):
    n += 1
    print(n * sign)



from math import copysign

max_n = int(input())
n, sign = 0, copysign(1, max_n)
print(n)
while n+1 < abs(max_n):
    n += 1
    print(int(n * sign))
