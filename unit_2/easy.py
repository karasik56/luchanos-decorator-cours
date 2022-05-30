"""1. Реализовать счетчик, который будет увеличиваться каждый раз,
 когда у нас осуществляется запуск функции суммирования."""
count = 0


def easy_unit2(a, b):
    global count
    count += 1
    return a + b


print(count)
print(easy_unit2(2, 2))
print(count)
print(easy_unit2(2, 2))
print(count)
print(easy_unit2(2, 2))
