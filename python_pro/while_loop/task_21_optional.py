"""
Наибольший делитель
Пользователь вводит два числа. Напиши программу,
которая находит и выводит на экран их наибольший
общий делитель с помощью алгоритма Евклида.
"""
a, b = int(input()), int(input())
while a and b:
    if a > b:
        a %= b
    else:
        b %= a
print("Наибольший делитель =", a+b)
