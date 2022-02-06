# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения ax^2+bx+c = 0 и возвращает его корни в порядке возрастания.


# объявление функции
def solve(a, b, c):
    from math import sqrt
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        return min(x1, x2), max(x1, x2)
    elif D == 0:
        return -b / (2 * a), -b / (2 * a)


# считываем данные
a, b, c = [int(input()) for i in range(3)]

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
