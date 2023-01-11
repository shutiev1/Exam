# 2 Определить функцию, которая проверяет является ли строка, введенная пользователем,
# целым числом. Решение задачи сдать ссылкой на GitHub.


def func(s):
    try:
        int(s)
        return True

    except ValueError:
        return False
print(func(input()))
