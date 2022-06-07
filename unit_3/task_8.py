"""8.1 Написать декоратор, который оборачивает функцию и подавляет возникновение любых ошибок.
 8.2 Параметризовать декоратор таким образом, чтобы декоратору можно было сообщить, какой именно тип ошибок стоит подавлять."""


def simple_decorator(exception):
    def inner(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as error:
                return f'Возникло исключение: {error}'

        return wrapper

    return inner


@simple_decorator(TypeError)
def my_func(a, b):
    return a / b


@simple_decorator(ZeroDivisionError)
def my_func_2(a, b):
    return a / b


print(my_func_2(5, 0))

print(my_func(5, ))
