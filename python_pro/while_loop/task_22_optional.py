"""
Число из умноженной суммы цифр

Напиши программу, которая вычисляет минимальное трёхзначное число,
которое равно сумме его цифр, умноженной на 50.
Цикл while должен использоваться один раз и без вложенных условий.
"""
n = 100
while (n // 100 + n % 10 + n % 100 // 10) * 50 != n:
    n += 1
print(n)