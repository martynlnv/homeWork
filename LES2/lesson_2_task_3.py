from math import ceil


def ceil_square(a, b):
    return ceil(a * b)


a = b = float(input("Сторона квадрата: "))
print(f"Площадь квадрата: {ceil_square(a, b)}")
