"""
Пользователь вводит число от 1 до 30 и степень, в которую хочет его возвести.
Используя цикл while, напиши программу, которая проверяет, верно ли введено
число.
Программа получает на вход число и его степень. Затем проверяет,
верно ли введено число.
Если да — возводит его в степень и выводит результат
на экран.
Если нет — выводит "Число введено неверно! Повторите ввод." и
просит повторить ввод (пользователь снова вводит число и степень).
"""
n = int(input())
pow_n = int(input())
while n < 1 or 30 < n:
    print("Число введено неверно! Повторите ввод.")
    n = int(input())
    pow_n = int(input())
print(n**pow_n)