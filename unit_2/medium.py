"""1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той,
 которая была решена для запуска функции суммирования.
2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться в качестве результата работы из объемлющей функции.
3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную. Напечатайте результат на экран. Что наблюдаете?
4. Осуществите вызов функции суммирования из полученной переменной."""

"""1"""
count_multy = 0
count_div = 0
count_sub = 0


def medium_unit2_multy(a, b):
    global count_multy
    count_multy += 1
    return a * b


def medium_unit2_div(a, b):
    global count_div
    count_div += 1
    return a / b


def medium_unit2_sub(a, b):
    global count_sub
    count_sub += 1
    return a - b