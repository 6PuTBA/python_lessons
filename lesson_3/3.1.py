"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "На ноль делить нельзя"


print(division(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
