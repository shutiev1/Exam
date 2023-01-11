# 1 Реализовать Рекурсию. Возведение числа x в степень y

def func(x, y):
    if y == 1:
        return x
    if y != 1:
        return x * func(x, y - 1)
x = int(input('Введите число: '))
y = int(input('Введите его степень: '))
print('Результат возведения в степень равен:', func(x, y))
