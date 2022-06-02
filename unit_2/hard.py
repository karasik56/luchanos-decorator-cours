"""Перенесите глобальный счетчик на уровень объемлющей функции.
 Будет ли работать наш код? Если да, то как поменялся смысл написанного кода?
  Если нет, то что надо изменить, чтобы всё заработало?"""


def outer_func():
    count = 0
    print(count)

    def hard_unit(a, b):
        nonlocal count
        count += 1
        print(count)
        return a + b

    hard_unit(1, 2)
    hard_unit(1, 2)


print(outer_func())

""" Для работы счетчика на уровне объемлющей функции необходимо использовать nonlocal count в теле той функции,
 где увеличиваем сам счетчик """
