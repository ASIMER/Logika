"""
Программа проверки.
Используя цикл while, напиши программу, запрашивающую  у пользователя
трёхзначное число, которое одновременно делится на 2 и на 3.
Если пользователь вводит неверное число, программа должна вывести строку
“Неверно, попробуй другое число!” и запросить ввод заново.
Если верно - вывести строку “Верно!”.
"""
n = int(input())
while n < 100 \
        or 1000 <= n \
        or n % 2 \
        or n % 3:
    print("Неверно, попробуй другое число!")
    n = int(input())
print("Верно!")